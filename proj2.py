import numpy as np
import matplotlib.pyplot as plt

a = 50
b = 50
c = a + b
step = 0.01
num_simulations = [10, 1000]

for num_games in num_simulations:
    results = {p: [] for p in np.arange(0, 1.01, step)}
    
    for p in results.keys():
        for _ in range(num_games):
            a_ruin = False
            capital_a = a
            capital_b = b

            while capital_a > 0 and capital_a < c:
                if np.random.random() < p:
                    capital_a += 1
                    capital_b -= 1
                else:
                    capital_a -= 1
                    capital_b += 1

                if capital_a == 0:
                    a_ruin = True
                    break

            results[p].append(a_ruin)

    average_results = {p: np.mean(result) for p, result in results.items()}
    p_values = list(average_results.keys())
    ruin_probabilities = list(average_results.values())

    plt.plot(p_values, ruin_probabilities)
    plt.title("Probability of ruin of player A vs. p")
    plt.xlabel("p - Probability of A taking 1$ from B")
    plt.ylabel("Probability of ruin of player A")
    plt.grid(True)

plt.show()