from scipy.special import lambertw
import numpy as np

gamma = np.array([0.1])

b = np.real((100*gamma + 1 - lambertw(np.e ** (100 * gamma + 1)))/gamma)

for i in range(len(b)):
    print(gamma[i], ":", b[i])