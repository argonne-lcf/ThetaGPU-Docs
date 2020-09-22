# ThetaGPU-Docs
Staging area for Theta-GPU documentation



# Containers

As of now, the nvidia containers with tensorflow 1, 2 and pytorch built against cuda11, cudnn8 are available in singularity format here:

```bash
$ ls /lus/theta-fs0/projects/datascience/thetaGPU/containers/
pytorch_20.08-py3.sif  tf1_20.08-py3.sif  tf2_20.08-py3.sif
```

Execute a container interactively like this:
`$ singularity exec --nv -B /lus:/lus /lus/theta-fs0/projects/datascience/thetaGPU/containers/tf1_20.08-py3.sif bash`
