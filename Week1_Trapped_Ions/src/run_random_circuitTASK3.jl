#!/usr/bin/env julia

using PastaQ
using ITensors
using Plots
using StatsBase
using LinearAlgebra, Statistics, Compat

function PastaQ.gate(::GateName"R"; theta::Real, phi::Real)
    [
        cos(theta / 2)    (-im * exp(-im * phi) * sin(theta / 2))
        (-im * exp(im * phi) * sin(theta / 2))     cos(theta / 2)
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

function run(N, depth)
    # Random circuit.
    gates = Vector{Tuple}[]

    for i in 1:depth
        one_qubit_layer = Tuple[]
        two_qubit_layer = Tuple[]

        for j in 1:N
            gate = ("R", j, (theta = 2pi * rand(), phi = 2pi * rand()))
            push!(one_qubit_layer, gate)
        end

        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N - 1)
            gate = ("M", (j, j + 1), (Theta = 2pi * rand(),))
            push!(two_qubit_layer, gate)
        end

        push!(gates, one_qubit_layer)
        push!(gates, two_qubit_layer)
    end

    psi = runcircuit(N, gates)
end

function task_3(psi, N)
    # generate computational basis (there is probably a simpler way to do this)
    all_perms(xs, n) = vec(map(collect, Iterators.product(ntuple(_ -> xs, n)...)))
    basis = all_perms(["↑","↓"], N)
    s = siteinds("S=1/2", N)

    # calculate inner products with all basis
    sum = 0.0
    probs = []
    for i in 1:2^N
        p = abs.(inner(psi, productMPS(s, basis[i])))^2
        push!(probs, p)
        # make sure probs add to one
        sum = sum + p
    end
    return probs
end


N = parse(Int, ARGS[1])

# Plot exact
f(x) = 1 - exp(-(2^N) * x)
plot(f,10^-3,1, linestyle=:dot, xaxis=:log, linecolor=:black, linewidth=4, labels="exact",legend=:bottomright)

depths = [1,2,4,8,16,32,64,128,256,512]
for i in depths
    psi = run(N, i)
    probs = task_3(psi, N)
    # plot and save
    plot!(sort(probs), (1:2^N) ./ 2^N, xaxis=:log, linewidth=2, labels=i)
end
png("../docs/images/CDF")

