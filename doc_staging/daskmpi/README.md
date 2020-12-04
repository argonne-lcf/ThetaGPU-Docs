# Dask-mpi on Theta

How to run [Dask-MPI](http://mpi.dask.org/en/latest/) on Theta at Argonne Leadership Computing Facility.

- [Install](#install)
- [Submit a batch job](#batch)
- [Run a script in an interactive session](#interactive)
- [Start a JupyterLab interactive session](#jlab)


<a id="install"></a>
## Install

1. `ssh` into one of Theta's login nodes

    ```bash
    ssh username@theta.alcf.anl.gov
    ```

1. Load Miniconda

    ```bash
    module load miniconda-3
    ```

1. Create a new conda environment

    ```bash
    conda create --name envname --clone $CONDA_PREFIX
    ```

1. Activate the environment

    ```bash
    source activate envname
    ```

1. Install `mpi4py` from the `alcf-theta` channel

    ```bash
    conda install -c alcf-theta mpi4py
    ```

1. Install the other dependencies from `conda-forge`

    ```bash
    conda install -c conda-forge dask dask-mpi bokeh jupyter Jupyterlab ipykernel ipyparallel pip
    ```

1. Download the files `start_daskmpi.py` and `dask_example.py` from this repository
    


### Local storage

If your dataset is larger than the combined memory of all compute nodes, Dask will spill excess data to disk. 
If you do not have write permission to local storage on the compute nodes, spilling to disk will be disabled by default, as explained [here](https://docs.dask.org/en/latest/setup/hpc.html#local-storage). 

See these [instructions](https://www.alcf.anl.gov/support-center/theta/theta-file-systems) on how to request access to local storage on Theta's compute nodes. 



<a id="batch"></a>
## Submit a batch job

This will run `dask_example.py` using 4 ranks on two nodes.

1. `ssh` into one of Theta's login nodes

    ```bash
    ssh username@theta.alcf.anl.gov
    ```

1. Submit a batch job on `n` nodes

    ```bash
    qsub -n 2 -t 30 -A datascience -q debug-cache-quad daskmpi_job.sh
    ```

    where the script `daskmpi_job.sh` is

    ```
    source activate envname
    cd dask_mpi/
    aprun -n 4 -N 2 python start_daskmpi.py dask_example.py
    ``` 

<a id="interactive"></a>
## Run a script in an interactive session

1. `ssh` into one of Theta's login nodes

    ```bash
    ssh username@theta.alcf.anl.gov
    ```

2. Submit an interactive job on `n` nodes

    ```bash
    qsub -n 2 -t 30 -I --attrs enable_ssh=1 -A datascience -q debug-cache-quad
    ```

    A shell opens up on one of the mom nodes

3. Activate the environment

    ```bash
    source activate envname
    ```

4. Run the example script. It is "[Exercise: Parallelize a for loop](https://tutorial.dask.org/01_dask.delayed.html#Exercise:-Parallelize-a-for-loop)" of the Dask tutorial on `dask.delayed`

    ```bash
    cd dask_mpi/
    aprun -n 4 -N 2 python start_daskmpi.py dask_example.py
    ```

    The output should be similar to the following: 

    ```
    Starting the scheduler
    Scheduler address: tcp://10.128.15.17:8786 on node nid03826
    Starting the workers
    Client status: <Client: 'tcp://10.128.15.17:8786' processes=3 threads=3, memory=608.02 GB>
    
    To connect to the Dask dashboard, execute the following command in a shell on your local machine:
        ssh -t -L 8787:localhost:8787 username@theta.alcf.anl.gov ssh -t -L 8787:localhost:8787 thetamom1 ssh -t -L 8787:localhost:8787 nid03826
    
    To open the Dask dashboard, go to:
        http://localhost:8787/status
    
    44
    elapsed time: 8.008632
    44
    elapsed time: 3.182807

    Code ran successfully.
    Successfully exited
    ```


#### Dask dashboard

You can connect to the Dask dashboard on `http://localhost:8787/status` in you browser after you run the `ssh` command printed in the above output message in a shell on your local machine.


<a id="jlab"></a>
## Start a JupyterLab interactive session

1. `ssh` into one of Theta's login nodes

    ```bash
    ssh username@theta.alcf.anl.gov
    ```

1. Submit an interactive job on `n` nodes

    ```bash
    qsub -n 2 -t 30 -I --attrs enable_ssh=1 -A datascience -q debug-cache-quad
    ```

    A shell opens up on one of the mom nodes

1. Activate the environment

    ```bash
    source activate envname
    ```

1. Run the `start_daskmpi.py` script without any argument to start a JupyterLab session

    ```bash
    cd dask_mpi/
    aprun -n 4 -N 2 python start_daskmpi.py
    ```

    Type `stop` to terminate the Dask session.

    The output should be similar to the following: 

    ```
    Starting the scheduler
    Scheduler address: tcp://10.128.15.25:8786 on node nid03834
    Starting the workers
    Client status: <Client: 'tcp://10.128.15.25:8786' processes=3 threads=3, memory=608.02 GB>
    Starting JupyterLab on the scheduler...
    
    To connect to JupyterLab and Dask dashboard, execute the following command in a shell on your local machine:
        ssh -t -L 7787:localhost:7787 -L 8787:localhost:8787 username@theta.alcf.anl.gov ssh -t -L 7787:localhost:7787 -L 8787:localhost:8787 thetamom1 ssh -t -L 7787:localhost:7787 -L 8787:localhost:8787 nid03834
    
    To open JupyterLab, go to (see log file /home/username/dask_logs/jupyterlab.log):
        http://localhost:7787/?token=39212debfed9bb19c78bf3d87f4a3b8d75bc2cce9087724e
    
    To open the Dask dashboard, go to:
        http://localhost:8787/status
    
    JupyterLab started. Type 'stop' to stop Dask: stop
    Successfully exited
    ```



#### JupyterLab and Dask dashboard

You can connect to JupyterLab on `http://localhost:7787/` in you browser and view the Dask dashboard on `http://localhost:8787/status` after you run the `ssh` command printed in the above output message in a shell on your local machine.


