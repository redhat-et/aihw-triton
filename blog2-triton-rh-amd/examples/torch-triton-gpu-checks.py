import torch
import triton

# Print Pytorch version
print("Pytorch version            : ", torch.__version__)

# Print Triton version
print("Triton version             : ", triton.__version__)

# Check if Pytorch detects the GPU
print("Pytorch detected GPU ?     : ", torch.cuda.is_available())

# Pytorch get GPU name
print("Pytorch detected GPU name  : ", torch.cuda.get_device_name())

# Triton backend 
print("Triton backend             : ", triton.runtime.driver.active.get_current_target().backend) 

# Pytorch get hip version 
print("Pytorch detected hip       : ", torch.version.hip) 

a = torch.tensor([1.0, 2.0, 3.0, 4.0], device="cpu")
print("Test CPU tensor is         : ", a)
print("                                is_cuda: ", a.is_cuda)

b = torch.tensor([1.0, 2.0, 3.0, 4.0], device="cuda")
print("Test GPU tensor is         : ", b)
print("                                is_cuda: ", b.is_cuda)

