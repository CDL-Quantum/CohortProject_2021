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

function PastaQ.gate(::GateName"E")
    [
        0    1
        1    0
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
            #println("Gate E" , ' ' , i, ' ', j)
            push!(err_qubit_layer, gate)
        end
        

        for j in 1:N
            if j != rdm
                gate = ("R", j, (theta=2pi*rand(), phi=2pi*rand()))
                #println(gate)
                #println("Gate R", ' ', i, ' ', j)
                push!(one_qubit_layer, gate)
                #println(one_qubit_layer)
                #println("")
            end
        end

        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N-1)
            if j != rdm
                gate = ("M", (j, j+1), (Theta=2pi*rand(),))
                #println(gate)
                #println(two_qubit_layer)
                #println("Gate M", ' ', i, ' ', j)
                push!(two_qubit_layer, gate)
                #println("")
            end
        end
        
        push!(gates, one_qubit_layer)
        push!(gates, two_qubit_layer)
        push!(gates, err_qubit_layer)
        
    end

    psi = runcircuit(N, gates)
end


N = 5 # number of qubits
depth = 5 # number of gates

psi = run(N, depth)

len = length(psi)
@show len
for i in 1:len
  @show psi[i]
end

all_perm(xs, n) = vec(map(collect, Iterators.product(ntuple(_ -> xs, n)...)))
basis_vectors = all_perm([0, 1], N)

sites = siteinds("S=1/2",N)
generate_state(state_vector) = [i == 1 ? "Up" : "Dn" for i=state_vector]
states = [generate_state(vec) for vec=basis_vectors]
basis_mps_array = [productMPS(sites, state) for state=states]

coefs = [dot(basis_mps, psi) for basis_mps=basis_mps_array]
probabilities = [norm(coef)^2 for coef=coefs]
sum(probabilities)

n = length(probabilities)

sizes = []
for i in 1:n
    size = probabilities[i]
    size = 100*size
    push!(sizes, size)
end

markers = ["circle"]

n = n

x = (range(0, stop = n, length = n + 2))[2:end - 1]

y = (range(1, stop = 1, length = n + 2))[2:end - 1]

scatter(x, 
        y, 
        m = markers, 
        markersize = sizes , 
        xlim = (0, n), 
        ylim = (0.5, 1.5), 
        legend = false, 
        xticks = [], 
        yticks = [],
        size = (700, 700), step = 20
)






