## Introduction
This repository can deploy and plot bit string probabilities of random circuits on the IonQ quantum machine via their API. The random circuit is modelled after the julia implementation found [here](https://github.com/CDL-Quantum/CohortProject_2021/blob/main/Week1_Trapped_Ions/run_random_circuit.jl).

For reference, you can find the IonQ API docs [here](https://docs.ionq.com/).

## Getting started

Hint: See [video tutorial of this step](https://share.vidyard.com/watch/GtNkHkpUTbV7rwEpjqNBxG?)

1. Create an account with ionq [here](https://cloud.ionq.com/)
2. Generate an API key [here](https://cloud.ionq.com/settings/keys)
3. Add your API key to [./src/config.js](./src/config.js). If your API key was `"test-key"`, the file should look something like:
    ```
    export default {
        API_KEY: "test-key",
        API_ENDPOINT: "https://api.ionq.co/v0.1/jobs"
    }
    ```
4. If you don't have npm or node, follow [these instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) to download them (node v13.2.0)
5. In this directory, run the following command:
    ```
    > npm install
    ```

## Deploy a random circuit on the IonQ trapped ion quantum computer

Hint: See [video tutorial of this step](https://share.vidyard.com/watch/8HEzZBBsWuMbV5GM7PqJd4?)

1. The easiest way is to use the npm script `create-default-job` (defined in [./package.json](./package.json)):
    ```
    > npm run create-default-job
    ```
    This will create a job named "default-qpu-job" with 8 qubits at a depth of 256 on the qpu.

### **If you want more fine grained control:** call the script manually and change any params you want (i.e. number of qubits, circuit depth, the machine type, job name):
1. Navigate into the scripts folder
    ```
    > cd src/scripts
    ```

2. Call the script defined in [./src/scripts/create-job.run.js](./src/scripts/create-job.run.js) (feel free to modify parameters):
    ```
    > node create-job.run.js --n-qubits 8 --circuit-depth 256 --machine-type qpu --name first-qpu-job
    ```
    * It might take some time for the quantum machines to run

    Alternatively, you can run it on a simulator with:
    ```
    > node create-job.run.js --n-qubits 8 --circuit-depth 256 --name first-simulator-job
    ```
    If you have problems with the above code try:
    ```
    > node create-job.run.js --help
    ```
3. Navigate to [https://cloud.ionq.com/jobs](https://cloud.ionq.com/jobs) to see the job

## Plotting the bit string probabilities of a completed job

Hint: See [video tutorial of this step](https://share.vidyard.com/watch/CwRhUHxqcjMATvQfebRmS3?)

1. Get the id of the job you wish to plot from [here](https://cloud.ionq.com/jobs)
2. Run the following command:
    ```
    > npm run analyze-job some-job-id
    ```
    - Be sure to replace `some-job-id` with the id of the job you found in part 1, for example:
    ```
    > npm run analyze-job 72e912d3-ea97-4f19-9cc0-8e6dbfa06ac4
    ```

## Resources

I made some video recordings outlining the above sections: 
1. [How to set the repository up](https://share.vidyard.com/watch/GtNkHkpUTbV7rwEpjqNBxG?)
2. [How to create a job](https://share.vidyard.com/watch/8HEzZBBsWuMbV5GM7PqJd4?)
3. [How to plot the cdf](https://share.vidyard.com/watch/CwRhUHxqcjMATvQfebRmS3?)

## Contact
If you have issues, shoot me an email at cleland.theo@gmail.com