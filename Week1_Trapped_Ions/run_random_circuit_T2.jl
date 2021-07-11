#!/usr/bin/env julia

using PastaQ
using Random
using Distributions
using NPZ

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

#using Random                       #Code for used fo generate the randoms numbers uniform(0,1)
#Random.seed!(12345)
#rn=rand(100000);
#npzwrite("r_numbers.npy", rn)

function run(N, depth, Dtheta)
    # Random circuit.
    rn=npzread("r_numbers.npy")
    gates = Vector{Tuple}[]
    location1=rand(DiscreteUniform(1, depth))  # Me dice en que capa aparece el bit flip
    it=1
    for i in 1:depth
        one_qubit_layer = Tuple[]
        two_qubit_layer = Tuple[]
        one_bit_flip = Tuple[]

        for j in 1:N
            gate = ("R", j, (theta=2pi*rn[it], phi=2pi*rn[it+1]))
            it=it+2
            push!(one_qubit_layer, gate)
                
        end
        
       
        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N-1)
            gate = ("M", (j, j+1), (Theta=2pi*rn[it]+Dtheta,)) #agregue el error sistematico en la compuerta de 2 qubits
            push!(two_qubit_layer, gate)
            it=it+1
            
        end
        
        # Bit flip in a random qubit and random postion in the circuit. 
        if flip==1            
           k=rand(DiscreteUniform(1, 4)) #Me dice sobre que qubit actua el bit flip  
           gate = ("R", k , (theta=pi, phi=-pi))
           push!(one_bit_flip, gate)        
        
           location2=rand(DiscreteUniform(1, 3)) # Me dice en que orden, dentro de la capa, aparece el bit flip
           if location1==depth
             if location2==1
               push!(gates, one_bit_flip)      
               push!(gates, one_qubit_layer)
               push!(gates, two_qubit_layer)
             elseif location2==2
               push!(gates, one_qubit_layer)
               push!(gates, one_bit_flip)        
               push!(gates, two_qubit_layer)             
             else         
               push!(gates, one_qubit_layer)
               push!(gates, two_qubit_layer)    
               push!(gates, one_bit_flip)        
             end
           else
             push!(gates, one_qubit_layer)
             push!(gates, two_qubit_layer)
             location1=location1+1   
           end     
         else  
          push!(gates, one_qubit_layer)
          push!(gates, two_qubit_layer)     
         end
    end
                            
    psi = runcircuit(N, gates)
 
end

N = parse(Int, ARGS[1])
depth = parse(Int, ARGS[2])
Nsamples = parse(Int, ARGS[3])
flip = parse(Int, ARGS[4])
Dtheta = parse(Float32, ARGS[5])
seed = parse(Int, ARGS[6])
Random.seed!(seed)

psi = run(N, depth, Dtheta)
samples = getsamples(psi, Nsamples)
npzwrite("samples.npy", samples)
