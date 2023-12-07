import numpy as np
import matplotlib.pyplot as plt

a = 50
b = 50
c = a + b
p_values = [1/5, 1/2, 4/5]

game_lengths = {p: [] for p in p_values}

for p in p_values:
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

        game_lengths[p].append(game_length)
    
    game_lengths[p] = sorted(game_lengths[p])
    #print(p, " : ", game_lengths[p])

for p in p_values:
    mean_length = np.mean(game_lengths[p])
    std_dev = np.std(game_lengths[p])
    
    
    plt.hist(game_lengths[p], bins=np.arange(min(game_lengths[p]), max(game_lengths[p]) + 2, 2) - 1, edgecolor='black', alpha=0.7)
    plt.xlabel('Game length')
    plt.ylabel('Num of simulations')
    plt.title(f'Players A game length distribution for p = {p}')
    plt.show()
    
    print("Probability : ", p)
    print("Mean Game Length: ", mean_length)
    print("Standard Deviation: ", std_dev)
    print()