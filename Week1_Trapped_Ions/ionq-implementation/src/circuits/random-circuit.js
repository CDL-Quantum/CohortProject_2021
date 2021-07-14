/**
 * This code aims to replicate the circuit from: https://github.com/CDL-Quantum/CohortProject_2021/blob/main/Week1_Trapped_Ions/run_random_circuit.jl
 * suitable to be sent to IonQ's quantum computer.
 * See https://docs.ionq.com/#operation/createJob for details on the input structure 
 * See https://docs.ionq.com/#section/Supported-Gates for details on the supported gates
 */

/**
 * 
 * @param {number} nQubits Number of qubits
 * @param {number} circuitDepth Depth of the circuit
 */
const randomCircuit = (nQubits, circuitDepth) => {
    const gates = []
    for (let i = 0; i < circuitDepth; i++) {

        for (let j = 0; j < nQubits; j++) {
            // Represent the single qubit gate as a random combination of successive rotations for x y and z dims
            const gateX = {
                gate: 'rx',
                target: j,
                rotation: Math.random()*2*Math.PI
            }
            const gateY = {
                gate: 'ry',
                target: j,
                rotation: Math.random()*2*Math.PI
            }
            const gateZ = {
                gate: 'rz',
                target: j,
                rotation: Math.random()*2*Math.PI
            }
            // oneQubitLayer.push([gateX, gateY, gateZ])
            gates.push(gateX)
            gates.push(gateY)
            gates.push(gateZ)
        }

        // Add the two qubit layer
        for (let j = i % 2; j < nQubits - 1; j+=2) {
            // Add the Ising XX gate: e^(-iθ X⊗X /2)
            const gate = {
                gate: 'xx',
                targets: [j, j + 1],
                rotation: Math.random()*2*Math.PI
            }
            gates.push(gate)
        }
    }
    return gates
}

export default randomCircuit