# Python virtual environments

## Base Python3.8 installation

A Miniconda base environment using Python 3.8 and containing optimized builds of
TensorFlow, PyTorch, and Horovod is available by loading the appropriate module:

```bash
module load conda/tensorflow
conda activate
```

## Extending with virtualenv

To extend this base environment with virtualenv and inherit the base enviroment packages, one can use the `--system-site-packages` flag:

```bash
python -m venv --system-site-packages my_env
source my_env/bin/activate
# Install additional packages here...
```
You can always retroactively change the `--system-site-packages` flag state for this
virtual environment by editing `my_env/pyvenv.cfg` and changing the value of the line
`include-system-site-packages = false`.

To install a different version of a package that is already installed in the base
environment, you can use:
```
pip install --ignore-installed  ... # or -I
```
The shared base environment is not writable, so it is impossible to remove or uninstall
packages from it. The packages installed with the above `pip` command should shadow those
installed in the base environment.

## Extending with conda
If you prefer to use `conda` to manage your environment, refer to the [conda
environments page](ml_frameworks/tensorflow/running_with_conda.md) for instructions on
cloning the base environment.

## Combining virtualenvs with containers
If you wish to extend the Python environment built into a Singularity container, refer
to the notes on [building on top of a container](building_python_packages.md).
