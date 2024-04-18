import numpy as np

def player_strategy(n_battalions, n_fields):
    battalions = np.zeros(n_fields, dtype=int)
    middle = n_fields // 2
    battalions[middle-1:middle+2] = n_battalions // 3
    remaining = n_battalions - sum(battalions)
    for i in np.random.choice(n_fields, remaining, replace=True):
        battalions[i] += 1
    np.random.shuffle(battalions)
    return battalions

def computer_strategy(n_battalions, n_fields):
    battalions = np.zeros(n_fields, dtype=int)
    battalions[0], battalions[-1] = n_battalions // 4, n_battalions // 4
    remaining = n_battalions - sum(battalions)
    for i in np.random.choice(n_fields, remaining, replace=True):
        battalions[i] += 1
    np.random.shuffle(battalions)
    return battalions
