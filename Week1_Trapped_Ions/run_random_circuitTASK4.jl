#!/usr/bin/env julia

using PastaQ
using ITensors
using Plots
using StatsBase
using LinearAlgebra, Statistics, Compat, Random

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

function run(N, depth, err)

    #Fix seed so for all errors the circuit is the same
    Random.seed!(1234)
    # Random circuit.
    gates = Vector{Tuple}[]

    for i in 1:depth
        one_qubit_layer = Tuple[]
        two_qubit_layer = Tuple[]

        for j in 1:N
            gate = ("R", j, (theta=2pi*rand(), phi=2pi*rand()))
            push!(one_qubit_layer, gate)
        end

        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N-1)
            gate = ("M", (j, j+1), (Theta=2pi*rand()+err,))
            push!(two_qubit_layer, gate)
        end

        push!(gates, one_qubit_layer)
        push!(gates, two_qubit_layer)

    end
    psi = runcircuit(N, gates)
end

function task_4(psi,N)

    #generate computational basis (there is probably a simpler way to do this)
    all_perms(xs,n) = vec(map(collect, Iterators.product(ntuple(_ -> xs, n)...)))
    basis = all_perms(["↑","↓"],N)
    s = siteinds("S=1/2",N)

    #calculate inner products with all basis
    sum = 0.0
    probs = Float64[]
    for i in 1:2^N
        p = abs.(inner(psi,productMPS(s,basis[i])))^2
        push!(probs, p)
        #make sure probs add to one
        sum = sum + p
    end
    return probs
end


N = parse(Int, ARGS[1])
depth = parse(Int, ARGS[2])

#run ideal case
psi = run(N,depth,0)
probs_ideal = task_4(psi,N)

errs = [0.0:0.01:0.1;]
shots = 10^6
FXEB = []
#run circuits with errors
for i in errs
    psi = run(N, depth, i)
    probs = task_4(psi,N)
    samps = []
    #sample bitstrings from circuit
    for j in 1:shots
        samp = StatsBase.sample(Weights(probs))
        #record ideal probability of that bitstring
        push!(samps,probs_ideal[samp])
    end
    print("\n",sum(samps))
    push!(FXEB,2^N*mean(samps)-1)
end
#plot and save
plot(errs, FXEB, linewidth=2,labels="FXEB")
png("FXEB")

