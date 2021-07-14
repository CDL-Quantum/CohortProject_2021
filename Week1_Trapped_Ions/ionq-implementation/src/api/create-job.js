import axios from 'axios'
import CONFIG from '../config.js'

/**
 * Creates a job on the IonQ machine using their API
 * @param {Number} nQubits Number of qubits to use
 * @param {String} machineType The type of machine to use (simulation or qpu)
 * @param {Array} circuit Array of objects specifically built for their API
 * @returns The response from the API 
 */
const createJob = async (nQubits, machineType, circuit, name) => {
    const config = {
        headers: {
            "authorization": `apiKey ${CONFIG.API_KEY}`,
            "contentType": "application/json",
        }
    }
    const data = {
        "lang": "json",
        "name": name || "default-name",
        "target": machineType,
        "shots": 1000,  // Controls precision of the histogram
        "body": { "qubits": nQubits, "circuit": circuit } 
    }
    return await axios.post(CONFIG.API_ENDPOINT, data, config)
}

export default createJob