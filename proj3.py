import numpy as np
import matplotlib.pyplot as plt

a_values = np.arange(1, 101)
b = 100 - a_values
p = 1/2

results = {a: [] for a in a_values}

for a in a_values:
    for _ in range(100):
        a_ruin = False
        capital_a = a
        capital_b = 100 - a

        while capital_a > 0 and capital_a < 100:
            if np.random.random() < p:
                capital_a += 1
                capital_b -= 1
            else:
                capital_a -= 1
                capital_b += 1

            if capital_a == 0:
                a_ruin = True
                break

        results[a].append(a_ruin)

average_results = {a: np.mean(result) for a, result in results.items()}
a_values = list(average_results.keys())
ruin_probabilities = list(average_results.values())

plt.plot(a_values, ruin_probabilities)
plt.title("Probability of ruin of player A vs initial capital of A")
plt.xlabel("Initial capital of A")
plt.ylabel("Probability of ruin of player A")
plt.grid(True)

plt.show()