# Running Tensorflow with Conda

Beware that these builds use CUDA and will not work on login nodes, which does not have CUDA installed as there are no GPUs.

## Tensorflow (master build)

Given A100 and CUDA 11 are very new, we have a build of the master branch of Tensorflow which includes better performance and support for these architectures.

Users can utilize them by running this setup script:
```bash
source /lus/theta-fs0/software/thetagpu/conda/tf_master/2020-11-11/mconda3/setup.sh
```
This will setup a conda environment with a recent "from scratch" build of the Tensorflow repository on the master branch. The `2020-11-11` in the path can be substituted for other dates found in the directory. Per the writing of this documetation the latest installation was `2021-01-08`. In the future, there will be newer builds available in that directory `/lus/theta-fs0/software/thetagpu/conda/tf_master/` so check there for newer installs and run the respective `mconda3/setup.sh` script to use it. The build directories will also include wheels for tensorflow and horovod in `/lus/theta-fs0/software/thetagpu/conda/tf_master/<date>/wheels` which can be used to `pip install <wheel-file>`.

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
