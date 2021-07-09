/**
 * Plots the probability histograms of a job on the IonQ machine via their API through the CLI. 
 * Make sure you are in the scripts folder:
 * > node plot-job-histogram.run.js --id [STRING]
 * 
 * For example:
 * > node plot-job-histogram.run.js --id 4d751fc4-5652-492b-8199-f67e201782dd
 */

 import yargs from 'yargs'
 import { getJob } from '../api/index.js'
 import plot from 'nodeplotlib'
 
 const run = async (jobId) => {
    let data
    try {
        ({ data } = await getJob(jobId))
    } catch (err) {
        console.error(err)
        return
    }
    if (!data || data.jobs.length === 0) {
        console.error(`Could not find job with given ID: ${jobId}`)
        return
    }
    // Make nice plots of the histograms
    try {
        const job = data.jobs[0]
        const histogram = job.data.histogram
        const x = Object.values(histogram)
        x.sort()
        const y = Array.from(x, (_, idx) => idx).map((idx) => idx / (x.length - 1))
        const plotData = [{x: x.map((val) => Math.log(val)), y, type: 'scatter'}];
        const layout = {
            title: `Cumulative Distribution of Bit String Probabilties for ${job.qubits} Qubits on the IonQ "${job.target}" Machine`,
        }
        plot.plot(plotData, layout);
    } catch (err) {
        console.error('An error occured generating histogram plot!')
        console.error(err)
    }
    return
 }
 
const { id } = yargs(process.argv.slice(2))
    .option('id', {
        type: 'string',
        description: 'Id of the job to fetch',
        required: true
    })
    .argv
 
run(id)