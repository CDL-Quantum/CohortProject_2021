### A Pluto.jl notebook ###
# v0.14.8

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    quote
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : missing
        el
    end
end

# ╔═╡ 48464f80-de88-11eb-003c-23eec447aadd
using PastaQ

# ╔═╡ b43c2cf8-46be-45e9-b665-fe63c422059f
using Plots

# ╔═╡ 8a4b603a-7777-41d7-bc88-60e1f4297128
using DataStructures

# ╔═╡ 746afd9e-11a7-4de7-b3ca-92bb48afacd6
using DataFrames

# ╔═╡ f484a087-d316-4e4e-9c40-30eab7d2220d
using Random

# ╔═╡ 670bfcb7-47aa-45df-bc03-fdf904d067fa
using Statistics

# ╔═╡ 6881ef69-03f4-4ff1-a658-36f75e9a24b2
md"""
# Task 1

The output states of deep random circuits are chaotic, in the sense that slight perturbations in the circuits can lead to very different sampling probabilities. Ref. 1 makes an analogy between the visual patterns produced by a laser and samples produced by a quantum computer:

``` Owing to quantum interference, the probability distribution of the bitstrings resembles a speckled intensity pattern produced by light interference in laser scatter, such that some bitstrings are much more likely to occur than others. ```

We will use this analogy to draw “speckle patterns” in order to visualize the states generated by perturbed random circuits.
"""

# ╔═╡ 90ad7498-318b-44cd-b115-403236feb775
plotly()

# ╔═╡ f7199713-4706-4d56-8934-12555a72b02b
md"""
We can create the gates using the function gate, lets create the gate R defined as

$R(\theta,\phi)=\begin{bmatrix}
cos\frac{\theta}{2} & -i e^{-i\phi}\sin\frac{\theta}{2} \\
-i e^{-i\phi}\sin\frac{\theta}{2}  & cos\frac{\theta}{2}
\end{bmatrix}$
"""

# ╔═╡ ebdc68cf-54d4-436a-b8c6-fd0bd3a86e78
function PastaQ.gate(::GateName"R"; theta::Real, phi::Real)
	[
		cos(theta/2)	(-im * exp(-im * phi) * sin(theta/2))
		(-im * exp(im * phi) * sin(theta/2))	cos(theta/2)
	]
end

# ╔═╡ df0e17eb-7c2d-4802-a0fa-7dfcfac1a9df
md"""
and the two qubits gate $M(\Theta)$, defined as follows

$M(\Theta)=\begin{bmatrix}
cos\Theta & 0 & 0 & -i sin\Theta \\
0  & cos\Theta & -i sin\Theta & 0 \\
0  & -i sin\Theta & cos\Theta & 0 \\
-i sin\Theta & 0 & 0 & cos\Theta 
\end{bmatrix}$

"""

# ╔═╡ 17e51f98-8fcb-485c-8024-57a74e2e0d2b
function PastaQ.gate(::GateName"M"; Theta::Real)
	[
		cos(Theta)	0 	0 	(-im * sin(Theta))
		0 	cos(Theta)	(-im * sin(Theta))	0
		0 	(-im * sin(Theta))	cos(Theta)	0
		(-im * sin(Theta))	0 	0 	cos(Theta)
	]
end

# ╔═╡ 89376f94-32bc-4a9b-a48d-6b2f71fa75e6
md"""
We can use the base function provided in the CDL github, we are going to include the measurements using the function __getsamples__
"""

# ╔═╡ 0dacb284-a62b-48c8-91be-e0a76af1ec5a
function run(N, depth,nshots=1024)
	#random circuit.
	gates = Vector{Tuple}[]
	
	for i in 1:depth 
		one_qubit_layer = Tuple[]
		two_qubit_layer = Tuple[]
		
		for j in 1:N
			gate = ("R", j, (theta=2*pi*rand(), phi=2pi*rand()))
			push!(one_qubit_layer, gate)
		end
		
		# Alternate start qubit for pairs
		idx_first = i % 2 + 1
		
		for j in idx_first:2:(N-1)
			gate = ("M", (j, j+1), (Theta=2pi*rand(),))
			push!(two_qubit_layer, gate)
		end
		
		push!(gates, one_qubit_layer)
		push!(gates, two_qubit_layer)
	end
	
	ψ = runcircuit(N, gates)
	getsamples(ψ,nshots)
end

# ╔═╡ e0ff650f-9c92-4de2-bad7-dcdd6f13bb54
md"""
Slide to select the number of qubits
"""

# ╔═╡ 850ab73d-0fb4-4fa4-a6fc-422ade076aa2
@bind nqubits html"<input type='range' min='0' max='12'>"

# ╔═╡ ce0b088b-e8a8-4959-be9d-3a4f9d13100c
md"""
and the depth of the circuit
"""

# ╔═╡ b5c67cd4-c52b-405c-a2a4-7ca0761da2a3
@bind circ_depth html"<input type='range' min='0' max='8'>"

# ╔═╡ 704ec14d-2b75-4577-89d2-85a065fe3669
nshots = 1024;

# ╔═╡ bbcddb0f-90b5-4bde-a584-8d4ff5d40c88
md"""
We have a random circuit with $nqubits and $circ_depth layers depth
"""

# ╔═╡ 80bca394-632e-49d3-8a1a-adb3b9af808a
measures = run(nqubits,circ_depth);

# ╔═╡ 622a57af-3cad-435d-b5f4-b8d456ddba6f
md"""
We can create a series of bit strings to represent the states that each qubit can assume, for $nqubits we have:
"""

# ╔═╡ 9740907f-1f36-473f-ad51-590c484ad073
begin
states_bin = []
map(0:2^nqubits -1) do i
	out = reverse(digits(i; base=2, pad=nqubits))
	push!(states_bin, out)
	md"bit-string for $i is $out"
end
end

# ╔═╡ c8a4c6c2-5736-4a41-9f95-60689371b671
md"""
With the state binary encoded and the measurements we can check the number of times each one of the states appears in our measurements and calculate the probability of the state appear
"""

# ╔═╡ 115b9bc3-bbc4-40db-9bdd-61134669758b
times_state_appear = counter(eachrow(measures));

# ╔═╡ 412fdfdc-c622-4a68-ac53-cc4f6b323868
map(1:2^nqubits) do i
	state = states_bin[i]
	ntimes = times_state_appear[state]
	md"The state $state shows $ntimes in $nshots shots"
end

# ╔═╡ e2b138d6-e634-490c-b5e2-aff772f1d14a
md"""
## Show is better than tell
We can create the so called speckle plot using the information gatther so far, The size of the dots is proportional to the probability of a particular state appears in our meassurements.
"""

# ╔═╡ 7f8f17fe-adf1-4f25-a60a-0e2a974b0659
md"""
### Number of qubits
"""

# ╔═╡ 2a933ad8-7e1f-48e3-819a-968ebfee07ca
@bind qubits2 html"<input type='range' min='0' max='8'>"

# ╔═╡ 5e91a88d-cdf3-4137-9d0b-ecff20af0402
md"""
### Circuit depth
"""

# ╔═╡ 0b427de6-9273-4fde-b995-f788196c57ea
@bind circ_depth2 html"<input type='range' min='0' max='8'>"

# ╔═╡ c20f31f1-919a-4dd5-998f-09c4e9c98ad9
md"""
### Number of shots
"""

# ╔═╡ b669b854-e8d0-418f-aaaa-ce372f1ed550
n_shots = 1024;

# ╔═╡ 43dc5186-f2c0-4364-804c-92a3762847d5
begin
measures_new = run(qubits2,circ_depth2,n_shots);
states_bin2 = []
map(0:2^qubits2 -1) do i
	out = reverse(digits(i; base=2, pad=qubits2))
	push!(states_bin2, out)
end
times_state_appear2 = counter(eachrow(measures_new));
end

# ╔═╡ 14b8736e-7d5f-42fb-89a7-1e744d136169
begin
scatter(1:2^qubits2,repeat([1],2^qubits2),ylim=(0.85,1.15), color = :bluesreds, 
		ms = [100*times_state_appear2[i]/n_shots for i in states_bin2],
		title="Speckle plot for $qubits2 qubits and $circ_depth2 layers circuit",
		legend = :false)
xticks!([1:2^qubits2;], [prod(string.(i)) for i in states_bin2],xrotation=90)
end

# ╔═╡ b5b2a823-dbf5-4c5b-8003-af329c6cebdd
md"""
# Task 2

The outputs of sufficiently deep random circuits are very sensitive to slight perturbations in the circuit parameters, which can be seen by inserting errors. For example, quantum computers are susceptible to bit-flip errors, modelled using

$\sigma =\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}$
"""

# ╔═╡ 4ebb2372-7e19-43f8-9555-5b7f27f20d91
function PastaQ.gate(::GateName"Flip")
	[
		0	1
		1   0
	]
end

# ╔═╡ 34fb8380-378c-451a-88b9-c66d0e5e3794
Random.seed!(42)

# ╔═╡ 7615b8f1-9dcb-4617-89f5-a8fab4b91e92
md"""
We need to create two functions based on the random circuit, one that will make the circuits and sample the probabilities without the bit flip and the exact same function but with an additional chance of a random bit to flip 
"""

# ╔═╡ 9ec63139-826c-4e67-9f01-087abefe1c91
function run_noflip(N, depth,θ=2pi*rand(),ϕ=2pi*rand(),Θ=2pi*rand(), nshots = 1024)
	#random circuit.
	gates = Vector{Tuple}[]
	
	for i in 1:depth 
		one_qubit_layer = Tuple[]
		two_qubit_layer = Tuple[]
		
		for j in 1:N
			gate = ("R", j, (theta=θ, phi=ϕ))
			push!(one_qubit_layer, gate)
		end
		
		
		# Alternate start qubit for pairs
		idx_first = i % 2 + 1
		
		for j in idx_first:2:(N-1)
			gate = ("M", (j, j+1), (Theta=Θ,))
			push!(two_qubit_layer, gate)
		end
		
		push!(gates, one_qubit_layer)
		push!(gates, two_qubit_layer)
	end

	ψ = runcircuit(N, gates)
	samples = getsamples(ψ,nshots)
	
	states_bits = []
	map(0:2^N -1) do i
		out = reverse(digits(i; base=2, pad=N))
		push!(states_bits, out)
	end
	states_freq = counter(eachrow(samples))
	
	states_prob = [100*states_freq[i]/nshots for i in states_bits]
	
	data = Dict([(prod(string.(i)), 100*states_freq[i]/nshots) for i in states_bits])
	
	return states_freq, data
	
end

# ╔═╡ fdcf8013-9b80-49b4-a876-747066e76c58
function run_withflip(N, depth,θ = 2pi*rand(),
					  ϕ = 2pi*rand(), Θ = 2pi*rand(), nshots = 1024,
					  threshold = 0.5)
	#random circuit.
	gates = Vector{Tuple}[]
	
	for i in 1:depth 
		one_qubit_layer = Tuple[]
		two_qubit_layer = Tuple[]
		
		for j in 1:N
			gate = ("R", j, (theta=θ, phi=ϕ))
			push!(one_qubit_layer, gate)
		end
		
		
		# Alternate start qubit for pairs
		idx_first = i % 2 + 1
		
		for j in idx_first:2:(N-1)
			gate = ("M", (j, j+1), (Theta=Θ,))
			push!(two_qubit_layer, gate)
		end
		
		push!(gates, one_qubit_layer)
		push!(gates, two_qubit_layer)
	end
	
	
	if rand() > threshold
		idx = rand(1:N)
		gate = ("Flip", idx)
		push!(gates, [gate])
	end	

	ψ = runcircuit(N, gates)
	samples = getsamples(ψ,nshots)
	
	states_bits = []
	map(0:2^N -1) do i
		out = reverse(digits(i; base=2, pad=N))
		push!(states_bits, out)
	end
	states_freq = counter(eachrow(samples))
	
	states_prob = [100*states_freq[i]/nshots for i in states_bits]
	
	data = Dict([(prod(string.(i)), 100*states_freq[i]/nshots) for i in states_bits])
	
	return states_freq, data
	
end

# ╔═╡ 75f9b352-a83d-4e9d-b7ee-cdcad65f96f6
md"""
We can make pseudo experiments and collect the outputs into two dataframes to later be randomly sampled. For simplicity we choose a simple circuit with 4 qubits and 4 layers, and the same random parameters are feed into the two circuits (no bit flip, bit flip), we run the pseudo experiments for 25 times
"""

# ╔═╡ 7dbb1403-21fb-4929-9f56-02741f7dd5fb
begin
df_noflip = DataFrame()
df_flip = DataFrame()
for i in 1:25
	theta = 2pi*rand()
	phi = 2pi*rand()
	Theta = 2pi*rand()
	a = run_withflip(4,4,theta,phi,Theta)
	b = run_noflip(4,4,theta,phi,Theta)
	append!(df_flip,DataFrame(a[2]))
	append!(df_noflip,DataFrame(b[2]))
end
end

# ╔═╡ 059d5649-67ab-499d-a450-0f4a5a65367e
df_flip

# ╔═╡ e936273a-42ba-4343-b11c-b3e237f93631
df_noflip

# ╔═╡ 5d0cc7f8-62fd-40fd-ae7c-a3dbac6d29ad
function plot_speckle(area_df,idx)
	p1 = scatter(1:2^4,repeat([1],2^4),ylim=(0.85,1.15), color = :bluesreds, 
		ms = [20*i/findmax(values(area_df[idx[1],:]))[1] for i in values(area_df[idx[1],:])],
		legend = :false)
	scatter!(1:2^4,repeat([1.05],2^4),color = :bluesreds, 
		ms = [20*i/findmax(values(area_df[idx[2],:]))[1] for i in values(area_df[idx[2],:])])
	scatter!(1:2^4,repeat([0.95],2^4),color = :bluesreds, 
		ms = [20*i/findmax(values(area_df[idx[3],:]))[1] for i in values(area_df[idx[3],:])])
	scatter!(1:2^4,repeat([1.1],2^4),color = :bluesreds, 
		ms = [20*i/findmax(values(area_df[idx[4],:]))[1] for i in values(area_df[idx[4],:])])
	scatter!(1:2^4,repeat([0.9],2^4),color = :bluesreds, 
		ms = [20*i/findmax(values(area_df[idx[5],:]))[1] for i in values(area_df[idx[5],:])])
	xticks!([1:2^4;], [string.(i) for i in keys(area_df[1,:])],xrotation=90)

	return p1
end

# ╔═╡ 5f8ed3e2-5c9c-4fa2-841d-b4f35e0aff6a
md"""
We randomly select 5 of the pseudo experiments for each case and display the speckle patterns to be compared
"""

# ╔═╡ 45845780-d2bf-4d66-9627-aa0a4ee6a13a
idx = [i for i in rand(1:25,5)];

# ╔═╡ b303f57e-ed3d-4a98-aab7-392c8d7ac58c
begin
	pa = plot_speckle(df_noflip,idx)
	pb = plot_speckle(df_flip,idx)
	plot(pa,pb,title = ["No bit fliped" "The bit maybe was fliped"])
end

# ╔═╡ e15ec2ba-f736-41d1-8b67-63736b9e026d
md"""
The left plot shows the specle patterns for the random circuits without the bit flipped sampled in different pseudo-experiments, while the right plot display the speckle patterns using the same parameters for used in the first circuit (no bit flip circuit), however now the circuit has a 50 % chance of have one random qubit to be fliped. 
"""

# ╔═╡ Cell order:
# ╠═48464f80-de88-11eb-003c-23eec447aadd
# ╠═b43c2cf8-46be-45e9-b665-fe63c422059f
# ╠═8a4b603a-7777-41d7-bc88-60e1f4297128
# ╠═746afd9e-11a7-4de7-b3ca-92bb48afacd6
# ╟─6881ef69-03f4-4ff1-a658-36f75e9a24b2
# ╠═90ad7498-318b-44cd-b115-403236feb775
# ╟─f7199713-4706-4d56-8934-12555a72b02b
# ╠═ebdc68cf-54d4-436a-b8c6-fd0bd3a86e78
# ╟─df0e17eb-7c2d-4802-a0fa-7dfcfac1a9df
# ╠═17e51f98-8fcb-485c-8024-57a74e2e0d2b
# ╟─89376f94-32bc-4a9b-a48d-6b2f71fa75e6
# ╠═0dacb284-a62b-48c8-91be-e0a76af1ec5a
# ╟─e0ff650f-9c92-4de2-bad7-dcdd6f13bb54
# ╟─850ab73d-0fb4-4fa4-a6fc-422ade076aa2
# ╟─ce0b088b-e8a8-4959-be9d-3a4f9d13100c
# ╟─b5c67cd4-c52b-405c-a2a4-7ca0761da2a3
# ╠═704ec14d-2b75-4577-89d2-85a065fe3669
# ╟─bbcddb0f-90b5-4bde-a584-8d4ff5d40c88
# ╠═80bca394-632e-49d3-8a1a-adb3b9af808a
# ╟─622a57af-3cad-435d-b5f4-b8d456ddba6f
# ╟─9740907f-1f36-473f-ad51-590c484ad073
# ╟─c8a4c6c2-5736-4a41-9f95-60689371b671
# ╠═115b9bc3-bbc4-40db-9bdd-61134669758b
# ╟─412fdfdc-c622-4a68-ac53-cc4f6b323868
# ╟─e2b138d6-e634-490c-b5e2-aff772f1d14a
# ╟─7f8f17fe-adf1-4f25-a60a-0e2a974b0659
# ╟─2a933ad8-7e1f-48e3-819a-968ebfee07ca
# ╟─5e91a88d-cdf3-4137-9d0b-ecff20af0402
# ╟─0b427de6-9273-4fde-b995-f788196c57ea
# ╟─c20f31f1-919a-4dd5-998f-09c4e9c98ad9
# ╠═b669b854-e8d0-418f-aaaa-ce372f1ed550
# ╟─43dc5186-f2c0-4364-804c-92a3762847d5
# ╟─14b8736e-7d5f-42fb-89a7-1e744d136169
# ╟─b5b2a823-dbf5-4c5b-8003-af329c6cebdd
# ╠═4ebb2372-7e19-43f8-9555-5b7f27f20d91
# ╠═f484a087-d316-4e4e-9c40-30eab7d2220d
# ╠═34fb8380-378c-451a-88b9-c66d0e5e3794
# ╟─7615b8f1-9dcb-4617-89f5-a8fab4b91e92
# ╠═9ec63139-826c-4e67-9f01-087abefe1c91
# ╠═fdcf8013-9b80-49b4-a876-747066e76c58
# ╠═670bfcb7-47aa-45df-bc03-fdf904d067fa
# ╟─75f9b352-a83d-4e9d-b7ee-cdcad65f96f6
# ╠═7dbb1403-21fb-4929-9f56-02741f7dd5fb
# ╠═059d5649-67ab-499d-a450-0f4a5a65367e
# ╠═e936273a-42ba-4343-b11c-b3e237f93631
# ╠═5d0cc7f8-62fd-40fd-ae7c-a3dbac6d29ad
# ╟─5f8ed3e2-5c9c-4fa2-841d-b4f35e0aff6a
# ╠═45845780-d2bf-4d66-9627-aa0a4ee6a13a
# ╟─b303f57e-ed3d-4a98-aab7-392c8d7ac58c
# ╟─e15ec2ba-f736-41d1-8b67-63736b9e026d