# Running PyTorch with Conda

Beware that these builds use CUDA and will not work on login nodes, which does not have CUDA installed as there are no GPUs.

## PyTorch (master build)

Given A100 and CUDA 11 are very new, we have a build of the master branch of PyTorch which includes better performance and support for these architectures.

Users can utilize them by running this setup script:
```bash
source /lus/theta-fs0/software/thetagpu/conda/pt_master/latest/mconda3/setup.sh
```
This will setup a conda environment with a recent "from scratch" build of the PyTorch repository on the master branch. The `latest` in the path is a symlink to a directory named by date that will be used to track our local builds. Per the writing of this documetation the only build uses `latest` points to `2020-11-25`. In the future, there will be newer builds available in that directory `/lus/theta-fs0/software/thetagpu/conda/pt_master/` so check there for newer installs and run the respective `mconda3/setup.sh` script to use it. If you find things break since the last time you ran, it may be because `latest` is now pointing at a newer PyTorch build.

This package will also include the latest Horovod tagged release.


## Installing Packages

### Using `pip install --user`

With the conda environment setup, one can install common Python modules using `pip install --users <module-name>` which will install packages in `$HOME/.local/lib/pythonX.Y/site-packages`.

### Using Conda Environments

If you need more flexibility, you can clone the conda environment into a custom path, which would then allow for root-like installations via `conda install <module>` or `pip install <module>`.

First, setup the conda environment you want to use as instructed above.

Second, clone the environment into a local path to which you have write access
```bash
conda create --clone $CONDA_PREFIX -p <path/to/env>
```
Then activate that environment:
```bash
conda activate <path/to/env>
```

One should then be able to install modules freely.
