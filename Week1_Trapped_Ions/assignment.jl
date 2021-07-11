#!/usr/bin/env julia

using PastaQ
using ITensors
using Random
using Plots
using LaTeXStrings

function PastaQ.gate(::GateName"F"; theta::Real, phi::Real)
    [
        cos(theta/2)    (-im * exp(-im * phi) * sin(theta/2) + 1)
        (-im * exp(im * phi) * sin(theta/2) + 1)     cos(theta/2)
    ]
end

function PastaQ.gate(::GateName"R"; theta::Real, phi::Real)
    [
        cos(theta/2)    (-im * exp(-im * phi) * sin(theta/2))
        (-im * exp(im * phi) * sin(theta/2))     cos(theta/2)
    ]
end

function PastaQ.gate(::GateName"M"; Theta::Real)
    [
        cos(Theta)    0    0    (-im * sin(Theta))
        0    cos(Theta)    (-im * sin(Theta))    0
        0    (-im * sin(Theta))    cos(Theta)    0
        (-im * sin(Theta))    0    0    cos(Theta)
    ]
end


function run(N, depth, rng=MersenneTwister(0), wbitflip=false, DTheta = 0.0)
    # Random circuit.
    gates = Vector{Tuple}[]

    if(wbitflip == true)
        rdepth = rand(1:depth)
        bitloc = rand(1:N)
    end

    for i in 1:depth
        one_qubit_layer = Tuple[]
        two_qubit_layer = Tuple[]

        if(wbitflip==true && rdepth == depth)
            for j in 1:N
                if(j == bitloc)
                    gate = ("F", j, (theta=2pi*rand(rng), phi=2pi*rand(rng))) 
                else
                    gate = ("R", j, (theta=2pi*rand(rng), phi=2pi*rand(rng)))
                end
                push!(one_qubit_layer, gate)
            end
        else
            for j in 1:N
                gate = ("R", j, (theta=2pi*rand(rng), phi=2pi*rand(rng)))
                push!(one_qubit_layer, gate)
            end
        end

        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N-1)
            gate = ("M", (j, j+1), (Theta=2pi*rand(rng)+DTheta,))
            push!(two_qubit_layer, gate)
        end

        push!(gates, one_qubit_layer)
        push!(gates, two_qubit_layer)
    end

    psi = runcircuit(N, gates)

    return psi
end


#############################################################################################
# Function calculates the probabilities associated with different basis states
# Arguments:
#   N = number of qubits
#   psi = MPS representing the state created by application of the quantum circuit 
# Return:
#   amp2 = array of probabilities
#############################################################################################

function getAmp2(N, psi)

    #Prepare site indices
    sites = siteinds("Qubit", N)
    offset = [1 for j in 1:N]

    amp2 = Vector{Float64}(undef,2^N)
    for i in 1:2^N
        state = digits(i-1, base=2, pad=N) |> reverse
        state += offset
        lval = abs(dot(psi,productMPS(sites,state)))^2
        amp2[i] = lval    
    end
  
    return amp2
end


#############################################################################################
# Function creates the speckle pattern associated with the probabilities of each basis state
# Arguments:
#   N = number of qubits
#   d = depth of the quantum circuit (needed only for plotting purposes)
#   amp2 = array representing the probabilties for each basis state
#   scale = controls the size of the circle in the speckle pattern
#   gsize = size of the plot area
# Return value:
#   plot object for plotting purposes 
#############################################################################################

function plotSpeckle(N, depth, amp2, scale=100, gsize=(400,50))

    p = plot([1],[1], seriestype = :scatter, markersize = scale*amp2[1], legend= false, xlims=(0,2^N+1), ylims = (0.5,1.5), markercolor = :red, axis=nothing, size=gsize) #, title="N = $N depth = $depth")
    for i in 2:2^N
        plot!(p,[i],[1], seriestype = :scatter, markersize = scale*amp2[i], legend = false, markercolor = :red)
    end

    return p
end


#############################################################################################
# Function for Task 1a
# Create a collage of speckles for different number of qubits and depths
#############################################################################################

function speckles()

    plotColl = Array{Plots.Plot{Plots.GRBackend},1}() 
    scales = [10,20,50,100]

    for (i,N) in enumerate([2,3,4,5])

        scale = scales[i]
        
        for depth in [4,16,32,64]
            psi = run(N, depth)
            amp2 = getAmp2(N, psi)
            p = plotSpeckle(N, depth, amp2, scale)
            push!(plotColl, p)
        end
    end

    #Create Collage
    newp = plot( (plotColl[i] for i in 1:size(plotColl)[1])..., size=(1800,600))
    display(newp)
end


#############################################################################################
# Function calculates the bond-dimension associated with the central link of the MPS encoding
# the wavefunction of interest for different depths
# Arguments:
#   N = number of qubits 
#   depths = array of circuit depths that will be simulated
#   seed = Seed for random number generator 
#############################################################################################

function studyBondDim_single(N, depths, seed=0)

    bdim = Vector{Int}(undef, size(depths)[1])    
    rng = MersenneTwister(seed)

    for (i,d) in enumerate(depths)
        psi = run(N, d, rng)
        bdim[i] = maxlinkdim(psi)         
    end
 
    p = plot(depths, bdim, seriestype = :scatter, markersize=5, legend=false, markercolor = :red)
    display(p)
end


#############################################################################################
# Function calculates the bond-dimension associated with the central link of the MPS encoding
# the wavefunction of interest for different depths
# Arguments:
#   Ns = array of number of qubits to simulate
#   depths = array of circuit depths that will be simulated
#   samples = number of samples to average over
#   seed = Seed for random number generator 
#############################################################################################

function studyBondDim(Ns, depths, samples=20, seed=0)

    rng = MersenneTwister(seed)
    plotColl = Array{Plots.Plot{Plots.GRBackend},1}() 
    colors = [:red, :blue, :green, :black, :orange, :magenta, :cyan]  
    
    rNs = Ns |> reverse #reversing for display purposes
    p = 0 
    for (j,n) in enumerate(rNs)
    
        samplebDim = fill(0.0, size(depths)[1])
        samplebDim2 = fill(0.0, size(depths)[1])

        for i in 1:samples

            lbdim = Vector{Int}(undef, size(depths)[1])
            for (i,d) in enumerate(depths)
                psi = run(n, d, rng)
                lbdim[i] = maxlinkdim(psi)
            end        

            samplebDim += lbdim
            samplebDim2 += lbdim.*lbdim
        end

        samplebDim /= samples
        samplebDim2 /= samples
        samplebDim2 = ((samplebDim2 - samplebDim.*samplebDim)/samples).^0.5

        if(p==0)
            p = plot(depths, samplebDim, seriestype = :scatter, markersize=5 + 0.2*n, legend=:topleft, markercolor = colors[j], yerror=samplebDim2, label="N = $n")
        else
            plot!(p, depths, samplebDim, seriestype = :scatter, markersize=5 + 0.2*n, legend=:topleft, markercolor = colors[j], yerror=samplebDim2, label="N = $n")
        end
    end

    display(p)    
end


#############################################################################################
# Function to create collage of speckles the results from randomly flipping a single qubit
# gate in a random location of the circuit 
# Arguments:
#   N = number of qubits to simulate
#   depth = circuit depth that will be simulated
#   samples = number of speckles to generate 
#   lout = Layout of collage 
#   seed = Seed for random number generator 
#############################################################################################

function bitFlipCompile(N, depth, samples=10, lout=(samples,1), seed=0)

    rng = MersenneTwister(seed)

    plotColl = Array{Plots.Plot{Plots.GRBackend},1}() 

    for i in 1:samples
        psi = run(N, depth, rng, true)
        amp2 = getAmp2(N, psi)
        push!(plotColl,plotSpeckle(N, depth, amp2))
    end

    #Create Collage
    newp = plot( (plotColl[i] for i in 1:samples)..., layout=lout, size=(1800,600))
    display(newp)
end


#############################################################################################
# Function to create the cumulant generating function associated with a single state of 
# basis of the quantum state created after application of quantum circuit. 
#
# Arguments:
#   N = number of qubits to simulate
#   depth = circuit depth that will be simulated
#   state = target state (as an integer)
#   samples = number of samples to obtain for state
#   dp = mesh increment for binning purposes
#   seed = Seed for random number generator 
# Optional:
#   plt = Used for plotting. If not supplied then a new plot is generated otherwise add
# Returns:
#   plt = Plot object
#   mval = probability values used for binning. 
#############################################################################################

function cgfScalingSingle(N, depth, state=2^(N-1), samples=1000, dp=0.001, seed=0; plt=nothing)

    rng = MersenneTwister(seed)
    sites = siteinds("Qubit", N)
    state = digits(2^(N-1), base=2, pad=N) |> reverse
    state += [1 for i in 1:N]

    pval = Vector{Float64}()
    for s in 1:samples        
        psi = run(N, depth, rng) 
        lval = abs(dot(psi,productMPS(sites,state)))^2
        push!(pval, lval)
    end

    pval = sort(pval)
    freq = Vector{Float64}()
    mval = Vector{Float64}()

    push!(freq,1)
    sval = 0.0
    lidx = 1
    push!(mval,sval+dp/2)

    for i in 1:samples
        if(pval[i]<=sval + dp)
            freq[lidx] += 1
        else
            sval += dp
            lidx += 1            
            push!(mval,sval + dp/2)
            push!(freq,1)
        end       
    end    

    freq = freq./samples
    #Show pdf
    #p1 = plot(mval,freq)

    #Show cgf
    cfreq = Vector{Float64}()
    push!(cfreq, freq[1])
    for i in 2:lidx
        push!(cfreq,cfreq[i-1] + freq[i])
    end
    if(plt === nothing)
        p2 = plot(mval, cfreq, xaxis = :log, label="depth = $depth", markersize=5, lw = 2)
        return p2, mval
    else
        plot!(plt,mval, cfreq, xaxis = :log, label="depth = $depth", markersize=5, lw = 2)
        return plt, mval
    end
end


#############################################################################################
# Function to create the cumulant generating function (CGF) associated with a single state of 
# basis of the quantum state created after application of quantum circuit. This is a compile
# function that plots the CGF for different circuit depths
#
# Arguments:
#   N = number of qubits to simulate
#   state = target state (as an integer)
#   samples = number of samples to obtain for state
#   dp = mesh increment for binning purposes
#   seed = Seed for random number generator 
#############################################################################################

function cgfScaling(N, state, samples=1000, dp = 0.0001, seed=0)

    plt = 0
    mval = nothing

    for (i,d) in enumerate([1, 4, 16, 64, 128, 256, 512])
        if(i==1)
            plt, mval = cgfScalingSingle(N, d, state, samples, dp, seed)
        else
            plt, mval = cgfScalingSingle(N, d, state, samples, dp, seed; plt)            
        end
    end
    
    tsize = 2^N
    theoryf = [1 - exp(-tsize*m) for m in mval]
    plot!(plt, mval, theoryf, xaxis = :log, label="theory", legend=:topleft, title="N: $N", markersize=5, lw=2)

    display(plt)
end


#############################################################################################
# Function calculates the lineraized cross entropy between two states 
# gate in a random location of the circuit 
# Arguments:
#   N = number of qubits to simulate
#   psi0 = First state as an MPS
#   psi = Second state as an MPS
# Returns:
#   fxeb = Linearized cross entropy value
#############################################################################################

function crossEntropyValue(N, psi0, psi)

    sites = siteinds("Qubit", N)
    offset = [1 for i in 1:N]
     
    avg = 0.0
    for s in 1:2^N        
        random_state = digits(s-1, base=2, pad=N) |> reverse
        random_state += offset #Get new binary representation of state

        pmps = productMPS(sites, random_state)
        amp2_0 = abs(dot(psi0,pmps))^2
        amp2_ns = abs(dot(psi,pmps))^2

        avg += amp2_0*amp2_ns 
    end

    fxeb = 2^N*avg - 1

    return fxeb 
end


#############################################################################################
# Function calculates the lineraized cross entropy between a state generated from a random
# circuit and for the same circuit with different systematic offsets in the angle of the 
# 2 qubit gates
# 
# Arguments:
#   N = number of qubits to simulate
#   depth = circuit depth
#   psi = Second state as an MPS
#   dsamples = Number of random quantum circuits to average over
#   seed = seed used for to initialize random number generator
#############################################################################################

function crossEntropy(N, depth, dsamples=20, seed=0)
    
    DThetas = 0.0:0.1:2pi
    
    fxebs = fill(0.0, size(DThetas)[1])
    sfxebs = fill(0.0, size(DThetas)[1])
        
    for i in 1:dsamples
     
        println("Sample ",i)
   
        #Get original state
        rng = MersenneTwister(seed + i)
        psi0 = run(N, depth, rng) 
    
        for (s,DTheta) in enumerate(DThetas)
    
            #Get DTheta state
            rng = MersenneTwister(seed + i) #Have to reset to make sure starting random circuit is identical
            psi = run(N, depth, rng, false, DTheta)

            fxeb = crossEntropyValue(N, psi0, psi)
            fxebs[s] += fxeb
            sfxebs[s] += fxeb*fxeb
        end
    end
   
    for (s,Dtheta) in enumerate(DThetas) 
        fxebs[s] /= dsamples
        sfxebs[s] = ((sfxebs[s]/dsamples - fxebs[s]*fxebs[s])/(dsamples-1))^0.5
    end
    
    plt = plot(DThetas, fxebs, yerror=sfxebs, xlabel="DTheta", legend=false, lw = 3)
    display(plt)
end


#-----------------------------------------------------------------------------------------------

#Task 1a
#speckles()

#Task 1b
N = 12
depth = 32 
#studyBondDim(2:2:N, 1:2:depth)

#Task 2
N = 5
depth = 16 
#bitFlipCompile(N, depth, 12, (4,3))

#Task 3
N = 8
#cgfScaling(N, 5)

#Task 4
N = 8
depth = 512
#crossEntropy(N, depth,1)

#Task 4b
N = 8 
depth = 128 
crossEntropy(N, depth, 200)
