import axios from 'axios'
import CONFIG from '../config.js'

/**
 * Gets a job on the IonQ machine using their API
 * @param {string} jobId Id of the job you want to get
 * @returns The fetched job
 */
const getJob = async (jobId) => {
    const config = {
        headers: {
            "authorization": `apiKey ${CONFIG.API_KEY}`,
            "contentType": "application/json",
        }
    }
    const data = {
        "params": { "id": jobId } 
    }
    return await axios.get(CONFIG.API_ENDPOINT, {...data, ...config})
}

export default getJob