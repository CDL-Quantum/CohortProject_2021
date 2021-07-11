# Used Packages
using PastaQ
using ITensors
using Plots
using StatsPlots

# Import Gates
include("gate_definitions.jl")

# run_random_circuit extension to support random bitflips
function run(N, depth, flipon)
    # Random circuit.
    gates = Vector{Tuple}[]
    if flipon == true
        td=rand(1:depth)
        tN=rand(1:N)
    end
    for i in 1:depth
        one_qubit_layer = Tuple[]
        two_qubit_layer = Tuple[]

        for j in 1:N
            gate = ("R", j, (theta=2pi*rand(), phi=2pi*rand()))
            push!(one_qubit_layer, gate)
            if flipon == true
                if j==tN && i==td
                    push!(one_qubit_layer, ("X", j))
                end
            end
        end

        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N-1)
            gate = ("M", (j, j+1), (Theta=2pi*rand(),))
            push!(two_qubit_layer, gate)
        end

        push!(gates, one_qubit_layer)
        push!(gates, two_qubit_layer)

    end
    psi = runcircuit(N, gates)
end

# Task 1
# This function extracts probabilitios
function get_Probs(psi,N)
    sites = siteinds("S=1/2", N)
    norm=0
    probs=zeros(0)
    for i=0:2^N-1
        x=digits(i,base=2,pad=N)
        states = [j+1 for j in x]
        phi = productMPS(ComplexF64,sites, states)
        y=inner(phi,psi)
        prob=y*conj(y)
        append!(probs,prob)
        norm=norm+prob
    end
    return probs
end

#Task 2
#This function runs the circuit multiple times
function runcirc_multiple(M,N,depth,flipon)
    results=Tuple[]
    for i=1:M
        psi=run(N,depth,flipon)
        push!(results,get_Probs(psi,N))
    end
    return results
end

#Task 4
#This functions create P(xi) samples for equation #1
function run_sampling(s,N,depth,flipon,delta)
    fxeb=zeros(2^N)
    for i=1:s
        psi=run_sysErr(N,depth,flipon,delta)
        fxeb=fxeb+get_Probs(psi,N)
    end
    fxeb=(2^N)*fxeb/s .-1
    return fxeb
end

#Task 4
#Applying the perturbation for series of DeltaThetas between zero to 2pi with the steps 2pi/gran
function perturb(gran,s,N,depth,flipon,site)
    deltas=zeros(0)
    avg_fxeb=zeros(0)
    for x=0:pi/gran:2pi
        append!(deltas,x)
        fxeb=run_sampling(s,N,depth,flipon,x)
        append!(avg_fxeb,fxeb[site])
    end
    return deltas,avg_fxeb
end
