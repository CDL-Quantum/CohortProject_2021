from julia import Julia

'''
for p in sys.path:
    if p.find('julia') != -1:
        break
else:
    print(f"ERR: Julia is not in PATH : {sys.path}")
    exit(-1)
'''
jl = Julia(compiled_modules=False)
x = jl.include("./run_random_circuit.jl")
print(x)
print(x(2, 2))
