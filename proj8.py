import numpy as np
import matplotlib.pyplot as plt

P = np.array([[0.64, 0.32, 0.04],
              [0.4, 0.5, 0.1],
              [0.25, 0.5, 0.25]])

Pi = np.array([1, 0, 0])

epsilon = 1e-5
n = 1
norm_values = []

while True:
    new_Pi = np.dot(P, Pi)
    
    norm = np.linalg.norm(new_Pi - Pi)
    norm_values.append(norm)
    
    if norm < epsilon:
        break
    else:
        Pi = new_Pi
        n += 1
        
print("Steady state after : ", n, " iterations")

plt.plot(range(n), norm_values)
plt.xlabel('Num of iterations')
plt.ylabel('Norm values')
plt.grid(True)
plt.show()