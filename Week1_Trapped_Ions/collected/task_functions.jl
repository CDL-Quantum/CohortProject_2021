# Used Packages
using PastaQ
using ITensors
using Plots
using StatsPlots

# Define our gates
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

function PastaQ.gate(::GateName"Z";)
    [
        1.00    0
        0     -1.00
    ]
end

function PastaQ.gate(::GateName"X";)
    [
        0    1.00
        1.00     0
    ]
end

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

function runcirc_multiple(M,N,depth,flipon)
    results=Tuple[]
    for i=1:M
        psi=run(N,depth,flipon)
        push!(results,get_Probs(psi,N))
    end
    return results
end
