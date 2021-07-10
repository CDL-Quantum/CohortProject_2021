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
        0    1
        1    0
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


	#Generate MPS (Matrix Product States
    psi = runcircuit(N, gates)
	println("psi", psi)
	
	return psi, gates
	
end

#N = parse(Int, ARGS[1])
#depth = parse(Int, ARGS[2])
N =4
depth = 1000

#run circuit with no errors
psi, gates= run(N, depth)
dump(psi)


#create gate string
gateTemp = ("X")

#apply gate flip randomly in circuit
one_qubit_layer = Tuple[]
for j in 1:N
	gateTemp = ("X", j, )
	push!(one_qubit_layer, gateTemp)
end

#Replace random gate with bit flip gate
badGateIdx = 901
saveGate = gates[badGateIdx];
gates[badGateIdx] =  one_qubit_layer



#re-run circuit
psi2 = runcircuit(N, gates)
dump(psi2)

#set gates back to error free
gates[badGateIdx] = saveGate
