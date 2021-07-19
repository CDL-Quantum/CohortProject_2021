#!/usr/bin/env julia

using PastaQ
using LinearAlgebra
using ITensors
using Plots

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

function run(N, depth)
    # Random circuit.
    gates = Vector{Tuple}[]
    
    rdms = []
    for i in 1:N
        push!(rdms, i)
    end
    
    
    rdm = rand((rdms))

    for i in 1:depth
        one_qubit_layer = Tuple[]
        two_qubit_layer = Tuple[]
        err_qubit_layer = Tuple[]
        
        begin (rdm < N)
        idx_err = rdm
        end
        
        for j in idx_err
            gate = ("E", j)
            push!(err_qubit_layer, gate)
        end
        

        for j in 1:N
            if j != rdm
                gate = ("R", j, (theta=2pi*rand(), phi=2pi*rand()))
                push!(one_qubit_layer, gate)
            end
        end

        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N-1)
            if j != rdm
                gate = ("M", (j, j+1), (Theta=2pi*rand(),))
                push!(two_qubit_layer, gate)
            end
        end
        
        push!(gates, one_qubit_layer)
        push!(gates, two_qubit_layer)
        push!(gates, err_qubit_layer)
        
    end

    psi = runcircuit(N, gates)
end

