# Running PyTorch with Conda

Beware that these builds use CUDA and will not work on login nodes, which does not have CUDA installed as there are no GPUs.

One can test these software in an interactive session:
```bash
qsub -I -n 1 -t 30 -A <project-name>
```

## PyTorch (master build)

Given A100 and CUDA 11 are very new, we have a build of PyTorch which includes better performance and support for these architectures.

Users can find the latest builds via the `module avail conda` command, which will list
 available builds
 such as `conda/2021-06-26` which is a module that was built on
`2021-06-26`. Use `module show conda/2021-06-26` or `module help conda/2021-06-26` to get
high level info on which versions of the key packages and libraries that this particular
module contains. This version can be used by
```bash
module load conda/2021-06-26  # loads conda into your environment, sets up appropriate CUDA libraries
conda activate # activates conda with python 
```

This will setup a conda environment with the "from scratch" build of PyTorch.

This package will also include builds of TensorFlow and Horovod tagged releases.

## Installing Packages

### Using `pip install --user`

With the conda environment setup, one can install common Python modules using `pip install
--users <module-name>` which will install packages in
`$PYTHONUSERBASE/lib/pythonX.Y/site-packages/` (by default set to `$HOME/.local/lib/pythonX.Y/site-packages`).

### Using Conda Environments

If you need more flexibility, you can clone the conda environment into a custom path, which would then allow for root-like installations via `conda install <module>` or `pip install <module>`.

1. Setup the conda environment you want to use as instructed above.
2. Create/edit your `$HOME/.condarc` file to include this these lines, replacing `<project-name` with your project name. By default, Conda will your `$HOME/.conda/*` area for caching files. Since home directories are limited to 100GB, this fills up quickly. This addition tells Conda to use your project space for cache storage instead.
```bash
pkgs_dirs:
  - /lus/theta-fs0/projects/<project-name>/conda/pkgs
envs_dirs:
  - /lus/theta-fs0/projects/<project-name>/conda/envs
```
3. Clone the environment into a local path to which you have write access
```bash
conda create --clone $CONDA_PREFIX -p <path/to/env>
```
4. Activate that environment:
```bash
conda activate <path/to/env>
```

One should then be able to install modules natively.
