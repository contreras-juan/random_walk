import random as rd
import numpy as np
import matplotlib.pyplot as plt

# set the simulation seed
rd.seed(65324)

random_walk = [1]

# generate random walk
for i in range(1,1000):
    noise = -1 if rd.random() < 0.5 else 1
    value = random_walk[i-1] + noise
    random_walk.append(value)

plt.plot(random_walk)
plt.show()