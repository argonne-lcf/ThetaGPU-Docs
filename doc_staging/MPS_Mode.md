# MPS Mode

MPS, or Multi-Process Server Mode, is an Nvidia supported mode for GPU computing on newer GPUs (volta or later).  Detailed documentation is available from nvidia [here](https://docs.nvidia.com/deploy/pdf/CUDA_Multi_Process_Service_Overview.pdf).

## When to Use MPS?

MPS is not always useful and productive.  If your application uses a majority of the GPU memory and/or compute cabability, MPS mode will provide little or no benefit.  On the other hand, if your application is largely a "hybrid" application - where both CPU and GPU have significant computational components - MPS can provide a significant benefit.  Some examples include:
- Deep Learning Frameworks during inference mode, where little or no communication is required but IO is significant.  In this case, it may be more performant to use small batches via MPS to more easily overlap IO and GPU compute
- Hybrid applications that are heavy on CPU operations with relatively small but frequent GPU offloads.  Even with collective operations, these operations can still have a performance benefit.  One example is using Sparse Convolutional Neural Networks.

## Enable MPS Mode

To use MPS, first you must enable an MPS service via `nvidia-cuda-mps-control -d`.  To stop the server, use `echo quit | nvidia-cuda-mps-control`.  Without this server running, MPS mode will not work: all CUDA calls get serialized between different processes and there is not a performance benefit.

## Running with MPS Mode on

To run your application, the easiest way is often to use MPI to launch processes, and map multiple processes per GPU.  If your code is not parallel, a for loop in bash can suffice, setting CUDA_VISIBLE_DEVICES appropriately.

### MPS Mode in when using Collectives

Nvidia's communication library, NCCL, supports at most one communicator device per GPU.  This means that if you need collective operations on the GPU, you must either change your code to do collective operations on the CPU or find another way to perform collectives.  In the case of something like `horovod`, this can be as simple as using MPI for collectives instead of `NCCL`.

