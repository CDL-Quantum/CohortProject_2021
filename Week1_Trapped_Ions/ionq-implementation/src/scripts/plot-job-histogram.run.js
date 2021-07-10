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
 
 const run = async (jobId, showTrueCdf) => {
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
        const { qubits, target } = job
        const probabilties = Object.values(histogram)
        const x = Array.from(probabilties, (_, idx) => idx).map((idx) => idx / (probabilties.length - 1))
        // Plot the histogram
        plot.stack([{
            x: Array.from(probabilties, (_, idx) => idx), 
            y: probabilties
        }], { 
            title: `Bit String Probabilties for ${qubits} Qubits on the IonQ "${target}" Machine`,
            xaxis: {
                title: 'Bit string'
            },
            yaxis: {
                title: 'Probability of bit string'
            }
        })
        // Plot the cdf 
        const cdf = [...probabilties]
        cdf.sort()
        plot.stack([{
            x: cdf.map(Math.log), 
            y: x
        }], { 
            title: `Cumulative Distribution of Bit String Probabilties for ${qubits} Qubits on the IonQ "${target}" Machine`,
            xaxis: {
                title: 'log(p)'
            },
        })
        if (showTrueCdf) {
            // True CDF for the specific case: 1 - e^(-2^N * p)
            const fn = (value) => 1 - Math.exp(-(2**qubits)*value)
            plot.stack([{
                x: cdf.map(Math.log), 
                y: cdf.map(fn), 
                type: 'scatter'
            }], { 
                title: `True Cumulative Distribution of Bit String Probabilties for 8 Qubits at Sufficient Depth`,
                xaxis: { title: 
                    'log(p)'
                }
            })
        }
        plot.plot();
    } catch (err) {
        console.error('An error occured generating histogram plot!')
        console.error(err)
    }
    return
 }
 
const { id, showTrueCdf } = yargs(process.argv.slice(2))
    .option('id', {
        type: 'string',
        description: 'Id of the job to fetch',
        required: true
    })
    .option('show-true-cdf', {
        type: 'boolean',
        description: 'Indicates if the true CDF will be plotted along side the computed one',
    })
    .default('show-true-cdf', false)
    .argv
 
run(id, showTrueCdf)