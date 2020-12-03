# Jupyter Instructions

1. From a `thetalogin` node: `ssh thetagpusn1` to login to a thetaGPU login node.
2. From `thetagpusn1`, start an interactive job (make sure to note which thetaGPU node the job gets routed to, `thetagpu21` in this example):

```bash
(thetagpusn1) $ qsub -I -A datascience -n 1 -t 01:00 -O interactive --attrs=pubnet=true
Job routed to queue "full-node".
Wait for job 10003623 to start...
Opening interactive session to thetagpu21
```

3. From the thetaGPU compute node, start a `jupyter` notebook:
   1. **Note:** This assumes you're in a suitable python environment containing `jupyter`, for more information on setting up a `conda` environment, see [Running Tensorflow with Conda](https://argonne-lcf.github.io/ThetaGPU-Docs/ml_frameworks/tensorflow/running_with_conda/)):

```bash
(thetagpu21) $ jupyter notebook&
```

4. From a new terminal (on your local machine):

```bash
$ export PORT_NUM=8889  # any number besides 8888 (the default) should work
$ ssh -L $PORT_NUM:localhost:8888 username@theta.alcf.anl.gov
(thetalogin) $ ssh -L 8888:localhost:8888 thetagpusn1
(thetagpusn1) $ ssh -L 8888:localhost:8888 thetagpu21
```

5. Navigating to `localhost:8889` (or whatever port number you chose above) on your local machine should then establish a connection to the jupyter backend!

