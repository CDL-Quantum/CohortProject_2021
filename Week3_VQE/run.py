import numpy as np
import matplotlib.pyplot as plt
from utility import get_molecular_data, obtain_PES
import time
import pandas as pd

class benchmark:
    def __init__(self,list_molecules=['h2'], list_basis=['sto-3g'], list_methods=['fci'],bond_lengths = np.linspace(0.2,2.6,15)):
        self.list_molecules = list_molecules
        self.list_basis = list_basis
        self.list_methods = list_methods
        self.bond_lengths = bond_lengths
        
        self.times = np.zeros((len(list_molecules),len(list_basis),len(list_methods)))
        self.results=np.zeros((len(list_molecules),len(list_basis),len(list_methods),len(bond_lengths)))
    
    def compute_all(self):
        for i_m,m in enumerate(self.list_molecules):
            print(f'{i_m+1} molecule out of {len(self.list_molecules)}')
            for i_b,b in enumerate(self.list_basis):
                print(f'{i_b+1} basis out of {len(self.list_basis)}')
                for i_f,f in enumerate(self.list_methods):
                    print(f'{i_f+1} method out of {len(self.list_methods)}')
                    tic = time.time()
                    self.results[i_m,i_b,i_f,:] = obtain_PES([m], self.bond_lengths, b, method=f)
                    toc = time.time()
                    self.times[i_m,i_b,i_f]= toc-tic                   
            
    
    def plot_all(self,i_b):
        
        colors = ['orange','purple','yellow','green']
        N = len(self.list_molecules)
        L = 3
        K = int(N/L) + 1 

        fig, axs = plt.subplots(K, L,figsize=(15,5))

        for i_m in range(N):
            ax = axs[i_m]

            ax.plot(self.bond_lengths, self.results[i_m,i_b,0,:], label=self.list_methods[0],color='k')
            s=15 
            for i_f in range(1,len(self.list_methods)):
                ax.scatter(self.bond_lengths, self.results[i_m,i_b,i_f,:], label=self.list_methods[i_f], color=colors[i_f-1],s=s)
                s*=0.9

            ax.set_title(f'{self.list_molecules[i_m]} dissociation, {self.list_basis[i_b]}')
            ax.set_xlabel('R, Angstrom')
            ax.set_ylabel('E, Hartree')
            ax.legend()
    
    def print_times(self,i_b):
        print('Duration of computation in seconds')
        T = np.squeeze(self.times[:,i_b,:])
        df = pd.DataFrame(T, index =self.list_molecules,columns =self.list_methods)
        return df
    
list_methods=['fci','hf','ccsd','cisd']
list_basis =['sto-3g','cc-pVDZ','cc-pVDZ','cc-pVTZ','cc-pVQZ','cc-pV5Z']
list_molecules=['h2','h2o','h4','lih','nh3','n2']
bench = benchmark(list_molecules=list_molecules,list_methods=list_methods)
bench.compute_all()

import pickle
with open('bench_molecules.pickle', 'wb') as f:
    pickle.dump(bench, f)