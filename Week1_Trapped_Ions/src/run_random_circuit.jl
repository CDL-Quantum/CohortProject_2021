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

function run(N::Int64, depth::Int64, nshots::Int64=0, rand_x::Bool=false, ret_params::Bool=false, ret_x_pos::Bool=false, ret_gates::Bool=false,
             in_r_param::Union{Vector{Tuple{Float64, Float64}}, Nothing}=nothing, in_m_param::Union{Vector{Float64}, Nothing}=nothing)
    # Random circuit.
    gates = Vector{Tuple}[]
    if ret_params
        r_params = Tuple{Float64, Float64}[]
        m_params = Float64[]
    end

    r_idx = 1
    m_idx = 1

    for i in 1:depth
        one_qubit_layer = Tuple[]
        two_qubit_layer = Tuple[]

        for j in 1:N
            if in_r_param !== nothing
                th = in_r_param[r_idx][1]
                phi = in_r_param[r_idx][2]
                r_idx += 1
            else
                th = 2pi*rand()
                phi = 2pi*rand()
            end
            if ret_params
                push!(r_params, (th, phi))
            end
            gate = ("R", j, (theta=th, phi=phi))
            push!(one_qubit_layer, gate)
        end

        # Alternate start qubit for pairs.
        idx_first = i % 2 + 1

        for j in idx_first:2:(N-1)
            if in_m_param !== nothing
                th = in_m_param[m_idx]
                m_idx += 1
            else
                th = 2pi*rand()
            end
            if ret_params
                push!(m_params, th)
            end
            gate = ("M", (j, j+1), (Theta=th,))
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
        ret_data = getsamples(psi, nshots)
    else
        ret_data = psi
    end

    if ret_params
        return (ret_data, r_params, m_params)
    elseif ret_x_pos
        return (ret_data, rand_pos, rand_qubit)
    elseif ret_gates
        return (ret_data, gates)
    else
        return ret_data
    end
end

#=
N = parse(Int, ARGS[1])
depth = parse(Int, ARGS[2])
shots = parse(Int, ARGS[3])

print(run(N, depth, shots))
=#
