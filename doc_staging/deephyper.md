# DeepHyper

For more details refer to the [DeepHyper documentation](https://deephyper.readthedocs.io/en/latest/index.html).

## Installation

The installation procedure of DeepHyper on ThetaGPU can be found on the official documentation of the software ["Installing DeepHyper on ThetaGPU](https://deephyper.readthedocs.io/en/latest/install/thetagpu.html).

## Example

From a ThetaGPU login node, you may then initiate an hyperparameter search using the `ray` evaluator through the `ray-submit` command line.  For instance:

```bash
deephyper start-project hps_demo
cd hps_demo/hps_demo
deephyper new-problem hps polynome2
mkdir exp && cd exp/
deephyper ray-submit hps ambs -w test_polynome2 -n 1 -t 15 -A datascience -q full-node -as ../SetUpEnv.sh -p hps_demo.polynome2.problem.Problem -r hps_demo.polynome2.model_run.run --max-evals 10 --num-cpus-per-task 1 --num-gpus-per-task 1 --n-jobs 16
```

For more details about how to use DeepHyper on ThetaGPU we refer to the official documentation of the software ["Running on ThetaGPU (ACLF)"](https://deephyper.readthedocs.io/en/latest/index.html).
