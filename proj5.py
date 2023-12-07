import numpy as np
import matplotlib.pyplot as plt

a = 50
b = 50
c = a + b
step = 0.01
p_values = np.arange(0, 1.01, step)

average_game_lengths = []

for p in p_values:
    game_lengths = []

    for _ in range(100):
        capital_a = a
        capital_b = b
        game_length = 0

        while capital_a > 0 and capital_a < c:
            if np.random.random() < p:
                capital_a += 1
                capital_b -= 1
            else:
                capital_a -= 1
                capital_b += 1
            game_length += 1

        game_lengths.append(game_length)

    average_length = np.mean(game_lengths)
    average_game_lengths.append(average_length)

plt.plot(p_values, average_game_lengths)
plt.title("Average Game Length vs. p")
plt.xlabel("p - Probability of A taking 1$ from B")
plt.ylabel("Average Game Length")
plt.grid(True)

plt.show()