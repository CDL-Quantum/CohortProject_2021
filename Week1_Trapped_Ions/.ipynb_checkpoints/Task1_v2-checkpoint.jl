#!/usr/bin/env julia

using PastaQ
using PyPlot
include("RandomCircuit.jl") #module that generate 

#If you want run this code, you must type three values below
N = parse(Int, ARGS[1]) #number of qubit = width
depth = parse(Int, ARGS[2]) #circuit depth
nshots = parse(Int, ARGS[3])

gates = run(N, depth) # Build gates

data= getsamples(gates, nshots, local_basis = ["Z"]) #sampling from gates with Z basis

M = [x[2] for x in data] #from data, we extract only value(not key) 

A = zeros(Int64, nshots) #string for saving decimal number transfroming binary number that obtained from getsamples 

# Binary to Decimal
for i in 1:nshots
    for j in 1:N
        A[i] += 2^(j-1)*M[i,j]
    end
end

Pr = zeros(Int,2^N) #we counts number of each binary number from string A, and save that number at Pr in order

for i in 1:nshots
    Pr[A[i] + 1] += 1
end

Pr_1 = zeros(2^N) #Pr_1 is probability from Pr.(Pr[i]/nshots)

for i in 1:2^N
    Pr_1[i]=Pr[i]/nshots
end

# plot speckle pattern using PyPlot
for i in 1:2^N
    scatter(i,0,color="red",linewidth=25.0*Pr_1[i])
end
axis("off")

show()