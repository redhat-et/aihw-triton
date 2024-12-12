import torch

# Ensure tensors are on the ROCm GPU
t1 = torch.randn((256, 256), device="cuda")
t2 = torch.randn((256, 256), device="cuda")

def foo(x, y):
    a = torch.sin(x)
    b = torch.cos(y)
    return a + b

opt_foo1 = torch.compile(foo)

print(opt_foo1(t1, t2))

