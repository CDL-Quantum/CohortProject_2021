/**
 * Deploys a circuit on the IonQ machine via their API through the CLI. 
 * Make sure you are in the scripts folder:
 * > node create-job.run.js --n-qubits [NUMBER] --circuit-depth [NUMBER] --machine-type [OPTIONAL STRING] --name [OPTIONAL STRING]
 * 
 * For example, to run an 8 qubit circuit of depth 4 on the simulator:
 * > node create-job.run.js --n-qubits 8 --circuit-depth 256 --name simulator-run
 * 
 * For example, to run an 8 qubit circuit of depth 4 on the quantum machine:
 * > node create-job.run.js --n-qubits 8 --circuit-depth 256 --machine-type qpu --name qpu-run
 */

import randomCircuit from '../circuits/random-circuit.js'
import yargs from 'yargs'
import { createJob } from '../api/index.js'

const run = async (nQubits, circuitDepth, machineType, name) => {
    const circuit = randomCircuit(nQubits, circuitDepth)
    try {
        const { data } = await createJob(nQubits, machineType, circuit, name)
        console.log('Success! Created job with id ', data.id)
    } catch (err) {
        console.error(err)
    }
}

const { nQubits, circuitDepth, machineType, name } = yargs(process.argv.slice(2))
    .option('n-qubits', {
        type: 'integer',
        description: 'Number of qubits to use',
        required: true
    })
    .option('circuit-depth', {
        type: 'integer',
        description: 'Depth of the generated circuit',
        required: true
    })
    .option('machine-type', {
        type: 'string',
        description: 'The type of machine to run on',
    })
    .option('name', {
        type: 'string',
        description: 'Optional name of the job'
    })
    .demand(['n-qubits', 'circuit-depth'])
    .number(['n-qubits', 'circuit-depth'])
    .check((argv) => {
        const { nQubits, circuitDepth} = argv
        if (!Number.isInteger(nQubits) || nQubits <= 0) {
          throw new Error("n-qubits must be an integer greater than zero")
        } else if (!Number.isInteger(circuitDepth) || circuitDepth <= 0) {
            throw new Error("circuit-depth must be an integer greater than zero")
        } else {
          return true
        }
      })
    .default('machine-type', 'simulator')
    .choices('machine-type', ['qpu', 'simulator'])
    .argv

run(nQubits, circuitDepth, machineType, name)