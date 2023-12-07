import numpy as np
import matplotlib.pyplot as plt

a = 50
b = 50
c = a + b
p_values = [1/2, 1/5]
L_sr = 85
n_values = [10, int(85/2), int(0.9*L_sr)]

def ruin_process(a, b, p, n):
    capital_a = a
    capital_b = b

    for _ in range(n):
        if np.random.random() < p:
            capital_a += 1
            capital_b -= 1
        else:
            capital_a -= 1
            capital_b += 1

        if capital_a <= 0 or capital_a >= c:
            break

    return capital_a

for p in p_values:
    for n in n_values: 
        capital_list = []
        for _ in range(1000):
            capital_a = ruin_process(a, b, p, n)
            capital_list.append(capital_a)
            
        capital_list = sorted(capital_list)
        plt.hist(capital_list, bins=np.arange(min(capital_list), max(capital_list) + 2, 2) - 1, edgecolor='black', alpha=0.7)
        plt.xlabel('Capital')
        plt.ylabel("Num of games")
        plt.title(f"Player A's Capital for p = {p} and steps = {n}")
        plt.legend()
        plt.show()