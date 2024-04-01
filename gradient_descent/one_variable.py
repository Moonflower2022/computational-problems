import autograd.numpy as np
import matplotlib.pyplot as plt
from autograd import elementwise_grad as egrad

def f(x):
    return np.exp(x)

print(egrad(f)(np.array([0])))
