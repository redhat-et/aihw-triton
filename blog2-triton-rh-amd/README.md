# Pytorch, Triton, AMD GPUs - Getting started in Red Hat containers

Basic POC for getting started with Pytorch, Triton, AMD GPU acceleration in Red Hat based containers.

## Description

For additional details and explanations, refer to the related blog post <link to be added here>.

### Pre-requisite

Physical Linux machine or VM with AMD Instinct GPUs (MI200, MI300X etc) and AMD GPU driver installed. 
 
### Building and executing

* Build the container image using the provided Containerfile
```
podman build -t triton-torch-amd-ubi -f ./Containerfile.ubi
```
* Run the container 
```
sudo podman run --rm -it     --device=/dev/kfd     --device=/dev/dri     --group-add=video --group-add=render   --security-opt=label=disable     --cap-add=SYS_PTRACE     --env HIP_VISIBLE_DEVICES=0  triton-torch-amd-ubi:latest
```
* Run an example programs 
From inside the running container, use python to run any of the example programs provided in the examples folder. These will get you going with developing Pytorch and Triton programs that leverage AMD GPU acceleration and run in a Red Hat container environment. Refer to the blog post for more details.
```
python ./examples/torch-triton-gpu-checks.py
```
Note: For the specific case of the torch-compile.py example, if you wiseh to see the generated Triton code, you will need to set the environment variable TORCH_COMPILE_DEBUG=1 before invoking python on torch-compile.py 
