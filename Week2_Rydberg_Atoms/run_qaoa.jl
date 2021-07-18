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

function convert_edge(edge::CartesianIndex{2})
    return (edge[1], edge[2])
end

function run_qaoa_circuit(Nv::Int64,
                          edges::Vector{CartesianIndex{2}},
                          durations::Vector{Float64},
                          dt::Float64)
    psi_t = zero_state(Nv)
    normalize!(durations, 1)

    interaction_term = map(1:size(edges)[1]) do i
        l,m = edges[i][1], edges[i][2]
        repeat(Nv,u*P1,(l,m))
    end |> sum

    for (i, d) in enumerate(durations)
        if i % 2 == 0 # Apply Mixing Hamiltonian (Omega = max, Delta = 0)
            h = interaction_term + Ω_max*sum(map(i->put(Nv,i=>X), 1:Nv))
        else # Apply Problem Hamiltonian (Omega = 0, Delta = max)
            h = interaction_term - δ_max*sum(map(i->put(Nv,i=>P1), 1:Nv))
        end
        psi_t = psi_t |> TimeEvolution(h, d * 100 / dt)
    end
    return psi_t
end
