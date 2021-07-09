#!/usr/bin/env julia

using PastaQ
using ITensors
using Random
using Plots

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

function plotSpeckle(N, amp2, scale=100, gsize=(400,100))

    p = plot([1],[1], seriestype = :scatter, markersize = scale*amp2[1], legend= false, xlims=(0,2^N+1), ylims = (0.5,1.5), markercolor = :red, axis=nothing, size=gsize)
    for i in 2:2^N
        plot!(p,[i],[1], seriestype = :scatter, markersize = scale*amp2[i], legend = false, markercolor = :red)
    end

    return p
end

function studyBondDim_single(N, depth, seed=0)

    bdim = Vector{Int}(undef, size(depth)[1])    
    rng = MersenneTwister(seed)

    for (i,d) in enumerate(depth)
        psi = run(N, d, rng)
        bdim[i] = maxlinkdim(psi)         
    end
    @show bdim
 
    p = plot(depth, bdim, seriestype = :scatter, markersize=5, legend=false, markercolor = :red)
    display(p)
end

function studyBondDim(N, depth, samples=20, seed=0)

    samplebDim = fill(0.0, size(depth)[1])
    samplebDim2 = fill(0.0, size(depth)[1])

    rng = MersenneTwister(seed)

    for i in 1:samples

        lbdim = Vector{Int}(undef, size(depth)[1])
        for (i,d) in enumerate(depth)
            psi = run(N, d, rng)
            lbdim[i] = maxlinkdim(psi)
        end        

        #@show lbdim

        samplebDim += lbdim
        samplebDim2 += lbdim.*lbdim
    end

    samplebDim /= samples
    samplebDim2 /= samples
    samplebDim2 = ((samplebDim2 - samplebDim.*samplebDim)/samples).^0.5

    p = plot(depth, samplebDim, seriestype = :scatter, markersize=5, legend=false, markercolor = :red, yerror=samplebDim2)
    display(p)
    
end

function bitFlipCompile(N, depth, samples=10, lout=(samples,1), seed=0)

    rng = MersenneTwister(seed)

    plotColl = Array{Plots.Plot{Plots.GRBackend},1}() 

    for i in 1:samples
        psi = run(N, depth, rng, true)
        amp2 = getAmp2(N, psi)
        push!(plotColl,plotSpeckle(N, amp2))
    end

    #Create Collage
    newp = plot( (plotColl[i] for i in 1:samples)..., layout=lout, size=(1000,600))
    display(newp)
end

function cgfScalingSingle(N, depth, samples=10000, dp = 0.001, seed=0)

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

    #p = histogram(pval; bins=0.0:dp:1.0)
    #display(p)
    
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
    p2 = plot(mval, cfreq, xaxis = :log, label="calculation")

    tsize = 2^N
    theoryf = [1 - exp(-tsize*m) for m in mval]
    plot!(p2, mval, theoryf, xaxis = :log, label="theory", legend=:topleft, title="Depth: $depth")
    #display(p2)

    return p2
end

function cgfScaling(N, samples=1000, dp = 0.001, seed=0)

    plotColl = Array{Plots.Plot{Plots.GRBackend},1}() 
    #for d in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    for d in [1, 4, 16, 32]
        push!(plotColl, cgfScalingSingle(N, d, samples, dp, seed))
    end

    fp = plot( (p for p in plotColl)...)
    display(fp)
end

function crossEntropyValue(N, depth, psi0, psi)

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

function crossEntropy(N, depth, seed=0)
    
    #Get original state
    rng = MersenneTwister(seed)
    psi0 = run(N, depth, rng) 


    DThetas = 0.0:0.5:2pi
    fxebs = Vector{Float64}()
    for DTheta in DThetas
    
        #Get DTheta state
        rng = MersenneTwister(seed) #Have to reset to make sure starting random circuit is identical
        psi = run(N, depth, rng, false, DTheta)

        fxeb = crossEntropyValue(N, depth, psi0, psi)
        push!(fxebs, fxeb)
        
        println(DTheta," ",fxeb)
    end
    
    plt = plot(DThetas, fxebs, xlabel="DTheta", legend=false)
    display(plt)
end


function crossEntropywDavg(N, depth, dsamples=20, seed=0)
    
    DThetas = 0.0:0.5:2pi
    
    fxebs = fill(0.0, size(DThetas)[1])
    sfxebs = fill(0.0, size(DThetas)[1])
        
    for i in 1:dsamples
        
        #Get original state
        rng = MersenneTwister(seed + i)
        psi0 = run(N, depth, rng) 
    
        for (s,DTheta) in enumerate(DThetas)
    
            #Get DTheta state
            rng = MersenneTwister(seed + i) #Have to reset to make sure starting random circuit is identical
            psi = run(N, depth, rng, false, DTheta)

            fxeb = crossEntropyValue(N, depth, psi0, psi)
            fxebs[s] += fxeb
            sfxebs[s] += fxeb*fxeb
        end
    end
   
    for (s,Dtheta) in enumerate(DThetas) 
        fxebs[s] /= dsamples
        sfxebs[s] = ((sfxebs[s]/dsamples - fxebs[s]*fxebs[s])/(dsamples-1))^0.5
    end
    
    plt = plot(DThetas, fxebs, yerror=sfxebs, xlabel="DTheta", legend=false)
    display(plt)
end


#-----------------------------------------------------------------------------------------------
#N = parse(Int, ARGS[1])
#depth = parse(Int, ARGS[2])

N = 3 
depth = 512 

#Task 1a
#psi = run(N, depth)
#amp2 = getAmp2(N, psi)
#p = plotSpeckle(N, amp2)
#display(p)

#Task 1b
#studyBondDim(N, 1:2:depth, 20)

#Task 2
#bitFlipCompile(N, depth, 12, (4,3))

#Task 3
#cgfScaling(N)

#Task 4
#crossEntropy(N, depth)

#Task 4b
crossEntropywDavg(N, depth, 50)
