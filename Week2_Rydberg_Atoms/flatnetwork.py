'''
    @Author: Ushnish Ray
    Copyright (2021) All Rights Reserved.
'''

import numpy as np
import simple_dmrg as dmrg
import scipy.sparse.linalg as las
import scipy.linalg as la

'''
    Class for graphing and lattice creation purposes
    Intialization Arguments:
        N = number of vertices
        l = maximum allowed range of interaction
        p1 = percentage of nearest neighbor interactions            
        p2 = percentage of long range interactions
'''
def random_flat_graph(L,l,p1,p2,u=1.34,seed=0):
    #Set Seed
    np.random.seed(seed)

    edges = {}
    w_ij = {}
    maxl = 0

    vtx_with_nn = np.random.randint(0,L-1,int(np.round(p1*L)))
    for i in vtx_with_nn:
        edges[(i,i+1)] = u
        w_ij[(i,i+1)] = np.random.rand()


    cnt = int(np.round((p2)*L))
    vtx_with_lr = np.random.randint(0,L-l,cnt) 
    for i in vtx_with_lr:            
        lc = np.random.randint(2,l+1)           
        tup = (i,(i+lc) % L)
        maxl = max(lc, maxl)

        if(tup[0]>tup[1]):
            tup = (tup[1],tup[0])

        edges[tup] = u
        w_ij[tup] = np.random.rand()       

    return edges, w_ij, maxl

def get_list(edges):
    return [[x[0],x[1]] for x in edges]

class FlatNetwork():
    
    def __init__(self, L, edges, w_ij, maxl):
        
        self.L = L                        
        
        #Variables needed for graph creation                
        self.edges = edges #Maintain a dictionary of edges
        self.w_ij = w_ij   #Maintain edge weights                    
        self.maxl = maxl   #Longest long-range connection       
                
        #Store mpos
        self.mpoc = None
                           
    def get_edges_in2d(self):
        #return edges in 2d-array format
        edges = np.zeros((self.L, self.L), dtype=bool)   
        
        for t in self.edges:
            edges[t[0],t[1]] = True;
            edges[t[1],t[0]] = True;
        
        return edges
    
    #Given graph construct MPO collection
    def get_mpos(self):
        if(not self.mpoc is None):
            return self.mpoc
        
        mpoc = []
        
        I = dmrg.I()
        N1 = dmrg.N(-1.0)
        N2 = dmrg.N(1.0)
        
        #left-most         
        lo = dmrg.MPO(1,2+self.maxl)
        lo.set(0,0,N1)
        pairs = [x for x in self.edges if(x[0]==0)]
        for pair in pairs:            
            sep = pair[1] - pair[0]
            lo.set(0,sep,dmrg.N(self.edges[pair]))
        lo.set(0,self.maxl+1,I)
        mpoc.append(lo)
        #print(pairs)
        #lo.show()
        
        #central pieces
        for i in range(1,self.L-1):        
            lo = dmrg.MPO(2+self.maxl,2+self.maxl)
            lo.set(0,0,I) 
            lo.set(1+self.maxl,1+self.maxl,I) 
            lo.set(1+self.maxl,0,N1) #on-site term
            
            #Must set transition states no matter what
            lo.set(1,0,N2)
            for j in range(self.maxl-1):
                lo.set(j+2,j+1,I)
            
            #now set last row
            pairs = [x for x in self.edges if(x[0] == i)]            
            for pair in pairs:
                sep = pair[1] - pair[0]                                                                       
                lo.set(self.maxl+1,sep,dmrg.N(self.edges[pair]))    
                
            mpoc.append(lo)
            #print(pairs)
            #lo.show()                    
        
        #right-most
        lo = dmrg.MPO(2+self.maxl,1)
        lo.set(0,0,I)
        lo.set(1,0,N2)
        lo.set(self.maxl+1,0,N1)        
        mpoc.append(lo)        
        #lo.show()
        
        self.mpoc = mpoc
        return mpoc            
        
    def run(self, cnvgThreshold = 1.0e-6, **kwargs):
        
        #Setup DMRG parameters
        dmrgp = dmrg.dmrgParams()
        dmrgp.L = self.L
        
        #Get MPOS and MPS
        mpos = self.get_mpos()
        mps = dmrg.MPS(dmrgp, allocate=False)
        
        dm = dmrg.DMRG(dmrgp,mps,mpos)
        
        #Sweep Schedule
        #sweepd = [2,5,10,15,20]
        #sweepi = [100,20,5,5,5]
        #sweepn = [1.0e-3,1.0e-4, 1.0e-4, 1.0e-4, 1.0e-5, 1.0e-5]
        
        sweepd = kwargs['sweepd'] if ('sweepd' in kwargs) else [1,2,2,2,3]
        sweepi = kwargs['sweepi'] if ('sweepi' in kwargs) else [5,5,5,5,5]
        sweepn = kwargs['sweepn'] if ('sweepn' in kwargs) else [1.0e-2,1.0e-3,1.0e-4,1.0e-5,1.0e-6]
        
        #Run
        sch = 0
        mps.setnewbd(sweepd[sch], noise=sweepn[sch])                
        mps.rightNormalize()        
            
        olde = 0.0
        for sch in range(len(sweepd)):
            print('Schedule: ',sch,' D = ', sweepd[sch])
            
            for i in range(sweepi[sch]):
                print('Beginning sweep: ',i,'of',sweepi[sch])
                newes = dm.sweep()
                newe = dm.energy()
                print('Sweep Energy: ',newe)
                if(abs(newe-olde)<cnvgThreshold):
                    olde = newe
                    break
                olde = newe
            
            if(self.L<12):
                amp = np.array(mps.getAmp())        
                ampl = np.where(np.abs(amp)>1.0e-8)[0]
                ampv = amp[ampl]
                config = [bin(x)[2:].zfill(L) for x in ampl]
                print(config)
                print(ampv**2)  
                        
            print('-----------')
        
            if(sch<len(sweepd)-1):
                mps.setnewbd(sweepd[sch+1])
                mps.rightNormalize()                
                dm.calcintR()
                olde = 0.0
       
        #return final mps for postprocessing
        return olde, mps
    
    #This is only for testing purposes. Do NOT use more than L = 12
    def runED(self, tol=1.0e-6):        
        mpos = self.get_mpos()        
        newmpo = dmrg.MPO.outer(mpos[0],mpos[1])
        #print(newmpo.ops[0][0])
        for i in range(2,self.L):            
            newmpo = dmrg.MPO.outer(newmpo,mpos[i])
            #print(newmpo.ops[0][0])
        #print('Final Hamiltonian is: ',newmpo.ops[0][0])
        
        lh = newmpo.op[0,0]
        [ev, psi0] = las.eigsh(lh,k=1,which='SA',maxiter=lh.shape[0]*10,tol=tol,ncv=100)        
        return ev, psi0
    
    #Also do a mean-field calculation
    def runMF(self, u = 1.35, threshold = 1.0e-6, maxiter=50, seed = 0):
                        
        #Seed
        np.random.seed(seed)
        
        #Start with random guess
        cs = np.random.randint(0,2,self.L)        
        #Compute MF values
        mfN = np.zeros(self.L)
        
        lastE = [0.0,0.0]
        lastState = [[],[]]
        
        for i in range(self.L):
            fjs = [x[1] for x in self.edges if(x[0] == i)] #Get all connected neighbors            
            sjs = [x[0] for x in self.edges if(x[1] == i)] #Sorted edge list so have to be careful                
            js = fjs + sjs                     
            mfN[i] = np.sum(cs[js])            
        
        for n in range(maxiter):
            
            #Solve local problem with MF guess            
            for i in range(self.L):                            
                le = -1.0 + u*mfN[i]                
                cs[i] = 1 if (le<0) else 0
            
            #Compute Energy
            uE = 0.0
            for pair in self.edges:
                uE += cs[pair[0]]*cs[pair[1]]*self.edges[pair]                
            tE = -1.0*sum(cs) + uE
            #print('** Current Energy: ',tE, 'for state: ',cs)                                                          
            print('** Current Energy: ',tE, end='')
            
            
            
            #Compute new MF values
            new_mfN = np.zeros(self.L)
            for i in range(self.L):
                fjs = [x[1] for x in self.edges if(x[0] == i)] #Get all connected neighbors            
                sjs = [x[0] for x in self.edges if(x[1] == i)] #Sorted edge list so have to be careful                
                js = fjs + sjs                     
                new_mfN[i] = np.sum(cs[js])            
            
            #print('Old MF: ',mfN, 'New MF: ',new_mfN)
            nrm1 = la.norm(new_mfN - mfN)            
            mfN = new_mfN
                        
            print(' Delta(mf) ',nrm1)                                    
            if(nrm1<threshold):
                break                        
            
            if(n>10 and abs(lastE[0]-tE)<1.0e-8): 
                break
            
            lastE[0] = lastE[1]
            lastE[1] = tE
            
            lastState[0] = lastState[1]
            lastState[1] = cs
        
        if(lastE[0]<lastE[1]):
            tE = lastE[0]
            cs = lastState[0]
        else:
            tE = lastE[1]
            cs = lastState[1]
            
        return tE,cs
    
if __name__ == '__main__':
    
    if(False):
        L = 6
        
        edges = {(0,1):1.35, (1,2):0.0, (2,3):1.35, (3,4):1.35, (4,5):1.35, (0,3):1.35, (1,4):0.0}
        wij = {}
        maxl = 3
        fn = FlatNetwork(L,edges,wij,maxl)
        mpos = fn.get_mpos()
                
        #Check that we are getting the correct energy
        mps_static1 = dmrg.MPS.scalarMPS([1, 1, 1, 1, 0, 0])
        e = dmrg.MPS.contractWithMPO(mps_static1, mpos, mps_static1)
        print('Energy calculated ',e)
    
    else:
        L = 50
        for u in [1.35]:

            edges, wij, maxl = random_flat_graph(L,min(10,L/2),0.5,0.5,u)

            fn = FlatNetwork(L,edges,wij,maxl)
            print(fn.edges)

            testMF = True
            if(testMF):
                print('\nTesting MF')
                tE, fstate = fn.runMF(u = u)
                print('MF Energy: ', tE)
                print('MF State: ', fstate)

            testDMRG = False
            if(testDMRG):
                print('\nTesting DMRG')
                e, mps = fn.run()    
                if(L<14):
                    amp = np.array(mps.getAmp())        
                    ampl = np.where(np.abs(amp)>1.0e-8)[0]
                    ampv = amp[ampl]
                    config = [bin(x)[2:].zfill(L) for x in ampl]

                    print(config)
                    print(ampv**2)        

            testED = False
            if(L<14 and testED):
                print('\nTesting ED')
                ev, psi0 = fn.runED()

                print('Exact Energy = ',ev)

                ampl = np.where(np.abs(psi0)>1.0e-8)[0]
                ampv = psi0[ampl]
                config = [bin(x)[2:].zfill(L) for x in ampl]

                print(config)
                print(ampv**2)
        