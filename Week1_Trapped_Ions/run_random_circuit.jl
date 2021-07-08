#!/usr/bin/env julia

using PastaQ

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

function PastaQ.gate(::GateName"X";)
    [
        0   1
        1   0
    ]
end

function run(N::Int64, depth::Int64, nshots::Int64=0, rand_x::Bool=false)
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
            gate = ("M", (j, j+1), (Theta=2pi*rand(),))
            push!(two_qubit_layer, gate)
        end

        push!(gates, one_qubit_layer)
        push!(gates, two_qubit_layer)
    end

    if rand_x
        rand_pos = rand(1:size(gates)[1]+1)
        rand_qubit = rand(1:N)
        gate = ("X", rand_qubit)
        insert!(gates, rand_pos, [gate])
    end

    psi = runcircuit(N, gates)
    if nshots > 0
        return getsamples(psi, nshots)
    else
        return psi
    end
end

#=
N = parse(Int, ARGS[1])
depth = parse(Int, ARGS[2])
shots = parse(Int, ARGS[3])

print(run(N, depth, shots))
=#
