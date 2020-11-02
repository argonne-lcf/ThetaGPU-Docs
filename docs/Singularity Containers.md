# Nvidia Containers

Nvidia delivers docker containers that contain their latest release of CUDA, tensorflow, pytorch, etc.  You can see the full support matrix for all of their containers here:

https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html

Docker is not runnable on ALCF's ThetaGPU system for most users, but singularity is.  To convert one of these images to signularity you can use the following command:

```bash
singularity build $OUTPUT_NAME $NVIDIA_CONTAINER_LOCATION
```
where `$OUTPUT_NAME` is typically of the form `tf2_20.09-py3.simg` and `$NVIDIA_CONTAINER_LOCATION` can be a docker url such as `docker://nvcr.io/nvidia/tensorflow:20.09-tf2-py3`

You can find the latest containers from nvidia here:
- Tensorflow 1 and 2: https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow
- Pytorch: https://ngc.nvidia.com/catalog/containers/nvidia:pytorch

For your convienience, we've converted these containers to singularity and they are available for August, 2020 and September 2020 here:
```bash
/lus/theta-fs0/software/thetagpu/nvidia-containers/
```

To extend the python libraries in these containers, please see https://github.com/argonne-lcf/ThetaGPU-Docs/blob/master/building_python_packages.md

For running with these containers, please see [NEEDS LINK]

For issues with these containers, please email support@alcf.anl.gov .
