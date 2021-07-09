# CDL Week 1 Cohort Project. Trapped Ions
Author: QuNovaComputing, Inc.
- - -

## 1. Installation Guide

### 1.0. Prerequisite
All based on python >= 3.6.

### 1.1. Install Julia
Go to [julia download page](https://julialang.org/downloads/) and follow the step.
Make sure your Julia binary directory to be added to `PATH`.

### 1.2. Install Python Libraries & PyJulia
Run the following on the terminal.
```shell
    $ pip install -r ./requirements.txt
    $ python ./install_pyjulia.py
```

- - -

## 2. Progress
### 2.1. Technical Tasks
- [x] Task 1 - Visualization of the distribution of measurement samples.
- [x] Task 2 - Single bit-flip error
- [x] Task 3 - Empirical distribution of `p`
- [x] Task 4 - Cross entropy benchmark fidelity for two-qubit gate error

### 2.2. Buiseness Application
- [x] Step 1
- [x] Step 2
- [x] Step 3
- [x] Step 4

### 2.3. Additional Challenges
- [x] Additional Challenge 1 - Animation for Task 2.
- [x] Additional Challenge 2 - Regeneration of fidelity from google paper.
- [ ] Additional Challenge 3 - Using IonQ machine.

- - -

## 3. Our Works
- Navigate main files (`./Task*.(ipynb|py)`) to see and reproduce the results of technical tasks.
### 3.1. Structure and Details
- `./src/` contains commonly used code fragments among main files.
- We modified `./src/run_random_circuit.jl` file from the original to support the following features:

    - Return the nshots of sample data from the simulation.
    - Optionally place a single X gate at random position and qubit.
    - Optionally return the randomly generated parameters for each gate.
    - Optionally return the position and qubit index of X gates which is randomly placed.
    - Optionally get the parameters for each gate to reproduce the same circuit previously simulated.

- `./src/julia_run_random_circuit.py` wraps the julia program to be accessed from python.
- `./src/utils.py` contains
    - functions to get histogram distribution from samples,
    - functions to get cross entropy fidelity from two distributions,
    - a function drawing speckle pattern circles from a distributions,
    - and some extra tool functions.
    
- `./task(3|4)_simulation.py` generates heavy simulation data which might take several hours.
It save the data in `./simulation_results/`, and main files will refer them.
- The outputs of additional challenge #1 are in `./animation_taskA1/`.
- `./dataset/` remains empty by gitignore, because the [dataset](https://datadryad.org/stash/dataset/doi:10.5061/dryad.k6t1rj8) is very large.
Download and extract by yourself.
  
- If you have a trouble when accessing to julia, because environment variable `PATH` could be different in venv,
  create `./envvir.py` containing a constant `JULIA_PATH = "path/to/julia/bin/"`.
