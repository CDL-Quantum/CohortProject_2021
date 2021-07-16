#!/usr/bin/env julia

using Yao
using Yao.ConstGate # needed for P1 = 0.5*(I - sigma_z) block

#=
H(t) = Ω(t) ∑_i σ_i^x - δ(t) ∑_i n_i + u ∑_ij n_i n_j
=#

const u = 1.35
const Ω_max = 1.89
const δ_0 = -1.0
const δ_max = 1.0

function get_edges(graph::Vector{NTuple{2, Float64}})
    Nv = size(graph)[1]
    edges = falses(Nv, Nv)
    for i in 1:(Nv-1)
        xi, yi = graph[i]
        for j in (i+1):Nv
            xj, yj = graph[j]

            dij = sqrt((xi - xj)^2. + (yi - yj)^2.)
            if dij <= 1.0
                edges[i,j] = true
            end
        end
    end
    return findall(edges)
end

function Ω(t::Float64)
    if 0 <= t <= 0.25
        return (Ω_max / 0.25) * t
    elseif 0.25 < t <= 0.69
        return Ω_max
    elseif 0.69 < t <= 1
<<<<<<< HEAD
        return - Ω_max * t / 0.31 + Ω_max * (1 + 0.69/0.31)
=======
<<<<<<< HEAD
<<<<<<< HEAD
        return Ω_max - Ω_max * (t-0.69) / 0.31 
=======
        return -Ω_max * t / 0.31 + 1.89/0.31
>>>>>>> 2b7b1b3f97b74e6999a1b6553b9f397bd4c2f001
=======
        return - Ω_max * t / 0.31 + Ω_max * (1 + 0.69/0.31)
>>>>>>> d9306be792ea6f70cbbd6af76ec7e7feae90ba5a
>>>>>>> main
    end
end

function δ(t::Float64)
    slope = (δ_0 - δ_max)/(0.25 - 0.69)
    if 0 <= t <= 0.25
        return δ_0
    elseif 0.25 < t <= 0.69
<<<<<<< HEAD
        return t * slope + (δ_max - slope * 0.69)
=======
<<<<<<< HEAD
        return (t-0.25) * (δ_max - δ_0)/0.44 + δ_0 
=======
        return t * slope + (δ_max - slope * 0.69)
>>>>>>> d9306be792ea6f70cbbd6af76ec7e7feae90ba5a
>>>>>>> main
    elseif 0.69 < t <= 1
        return δ_max
    end
end 

function hamiltonian(graph::Vector{NTuple{2, Float64}}, edges::Vector{CartesianIndex{2}}, t::Float64)
    # the UD-MIS Hamiltonian
    Nv = size(graph)[1] # number of vertices

    interaction_term = map(1:size(edges)[1]) do i
        l,m = edges[i][1], edges[i][2]
        repeat(Nv,u*P1,(l,m))
    end |> sum
    interaction_term - δ(t)*sum(map(i->put(Nv,i=>P1), 1:Nv)) + Ω(t)*sum(map(i->put(Nv,i=>X), 1:Nv))
end

function run_annealing(graph::Vector{NTuple{2, Float64}}, edges::Vector{CartesianIndex{2}}, dt::Float64)
    psi_t = zero_state(size(graph)[1])
    for t in 0:dt:1.0
        h = hamiltonian(graph, edges, t)
        psi_t = psi_t |> TimeEvolution(h, dt * 100)
    end
    return psi_t
end

graph = [(0.3461717838632017, 1.4984640297338632), 
         (0.6316400411846113, 2.5754677320579895), 
         (1.3906262250927481, 2.164978861396621), 
         (0.66436005100802, 0.6717919819739032), 
         (0.8663329771713457, 3.3876341010035995), 
         (1.1643107343501296, 1.0823066243402013)
        ]
edges = get_edges(graph)
dt = 0.001

psi = run_annealing(graph, edges, dt)
<<<<<<< HEAD
=======
<<<<<<< HEAD
samples = measure(psi; nshots=1024)
@show samples
=======
>>>>>>> main
open("task2_data.dat","w") do io
    for sample in measure(psi; nshots=10_000)
        println(io, sample)
    end
end

#samples = measure(psi; nshots=10)
<<<<<<< HEAD
#@show samples
=======
#@show samples
<<<<<<< HEAD
>>>>>>> d9306be792ea6f70cbbd6af76ec7e7feae90ba5a
=======
>>>>>>> 5957b6928520a26ac27558630773657297bc0d97
>>>>>>> main
