#!/usr/bin/env julia

using PastaQ
using ITensors
using PyPlot

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
    insert!(gates,(abs(rand(Int)) % size(gates)[1] + 1),[("X",(abs(rand(Int)) % N) + 1)])

    psi = runcircuit(N, gates)
end

# contruct MPS of number X
function x_mps(N, x)
    gates = Vector{Tuple}[]
    one_qubit_layer = Tuple[]
    # create circuit
    for i in 1:N
        if x % 2 == 1
            gate = ("X",i)
            push!(one_qubit_layer, gate)
        end
        x = x÷2
    end
    push!(gates, one_qubit_layer)
#     @show gates
    psi = runcircuit(N, gates)
end




N = parse(Int, ARGS[1])
depth = parse(Int, ARGS[2])




ψ = run(N, depth)

pr = Vector{Float64}(undef,2^N)
for i in 1:2^N
    temp_psi = x_mps(N,i-1)
    pr[i]= real(inner(temp_psi,ψ)*inner(temp_psi,ψ)')
end

subfig = figure("pyplot_subplot_mixed",figsize=(10,10)) # Create a new blank figure
subplot(511)
for i in 0:2^N-1
    scatter(i,0,color="red",linewidth=40.0*pr[i+1])
end
axis("off")


subplot(512)
ψ = run(N, depth)
for i in 1:2^N
    temp_psi = x_mps(N,i-1)
    pr[i]= real(inner(temp_psi,ψ)*inner(temp_psi,ψ)')
end
for i in 0:2^N-1
    scatter(i,0,color="red",linewidth=40.0*pr[i+1])
end
axis("off")

subplot(513)
ψ = run(N, depth)
for i in 1:2^N
    temp_psi = x_mps(N,i-1)
    pr[i]= real(inner(temp_psi,ψ)*inner(temp_psi,ψ)')
end
for i in 0:2^N-1
    scatter(i,0,color="red",linewidth=40.0*pr[i+1])
end
axis("off")

subplot(514)
ψ = run(N, depth)
for i in 1:2^N
    temp_psi = x_mps(N,i-1)
    pr[i]= real(inner(temp_psi,ψ)*inner(temp_psi,ψ)')
end
for i in 0:2^N-1
    scatter(i,0,color="red",linewidth=40.0*pr[i+1])
end
axis("off")

subplot(515)
ψ = run(N, depth)
for i in 1:2^N
    temp_psi = x_mps(N,i-1)
    pr[i]= real(inner(temp_psi,ψ)*inner(temp_psi,ψ)')
end
for i in 0:2^N-1
    scatter(i,0,color="red",linewidth=40.0*pr[i+1])
end
axis("off")

show()
# gcf()