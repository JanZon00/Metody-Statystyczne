import numpy as np
import matplotlib.pyplot as plt

p_values = [1/2, 1/5]
players_values = [(50, 50), (25, 75)]

def ruin_process(a, b, p):
    capital_a = a
    capital_b = b
    capital_a_list = [capital_a]
    capital_b_list = [capital_b]

    for _ in range(100):
        if np.random.random() < p:
            capital_a += 1
            capital_b -= 1
        else:
            capital_a -= 1
            capital_b += 1

        if capital_a <= 0 or capital_a >= 100:
            break
        
        capital_a_list.append(capital_a)
        capital_b_list.append(capital_b)
        

    return (capital_a_list, capital_b_list)

for p in p_values:
    for value in players_values:
        capital_list = ruin_process(value[0], value[1], p)
        capital_a_list = capital_list[0]
        capital_b_list = capital_list[1]
        plt.plot(range(1, len(capital_a_list) + 1), capital_a_list, label="capital of a")
        plt.plot(range(1, len(capital_b_list) + 1), capital_b_list, label="capital of b")
    
        plt.xlabel('Steps')
        plt.ylabel("Player A's Capital")
        plt.title(f"Player's Capital for p = {p}")
        plt.legend()
        plt.show()