import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

u1 = np.random.uniform(low = 0.0, high = 1.0, size = 10000) 
u2 = np.random.uniform(low = 0.0, high = 1.0, size = 10000) 

#algorytm Boxa-Mullera
R = np.sqrt(-2 * np.log(u1))
theta = 2 * np.pi * u2
x = R * np.cos(theta)
y = R * np.sin(theta)
X = np.concatenate((x, y), axis=0)

plt.hist(X, bins=100, density=True, alpha=0.6, color='b', label='Histogram')

x = np.linspace(-5, 5, 100)
pdf = norm.pdf(x, loc=0, scale=1)

plt.plot(x, pdf, 'r', linewidth=2, label='Dystrybuanta teoretyczna')
plt.grid(True)
plt.legend()
plt.show()