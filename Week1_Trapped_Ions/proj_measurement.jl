#!/usr/bin/env julia

# Convert Matrix -> Vector to extract information easily
function BinaryToDecimal(M,N)
    idx = zeros(Int8,size(M)[1],1)
    for i in 1:N
        idx += M[:,i].*2^(i-1)
    end
    
    return idx
end

# From sampling of state to Decimal representation vector
function execute(ψ,N,shots,basis)
    #=
    basis (Str) = "X", "Y", or "Z" basis for the projective measurement
    =#
    data = getsamples(ψ, shots ,local_basis=[basis])
    B = last.(data)
    C = BinaryToDecimal(B,N)
    return C
end

# Get Probabilities dictionary
function get_probabilities(N,qc)
    #= 
    N = number of qubits
    qc = Result of the quantum circuit, i.e. outcome of execute() 
    =#
    # Initialize Count variable
    Count = Dict{Int64,Int64}()
    for i in 0:2^N-1
        push!(Count,i=>0)
    end
    
    # Count the number of 0s and 1s
    Keys = keys(Count)
    for k in Keys
        Count[k]+=count(i->(i==k),qc)
    end
    
    # Convert the count to probability
    Prob = Dict{Int64,Float64}()
    Total_shots = sum(values(Count))
    for i in 0:2^N-1
        push!(Prob,i=>(Count[i]/Total_shots))
    end
    
    return sort(Prob)
end