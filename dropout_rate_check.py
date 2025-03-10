from random import randint
from math import sqrt, ceil, floor
from collections import Counter

c = []
for _ in range(100):
    N = randint(1, 1012)
    W = randint(1, 109)
    H = randint(1, 109)
    
    square = N * W * H
    side = ceil(sqrt(square))

    n_weight = floor(side / W)
    n_height = floor(side / H)
    n_square = n_weight * n_height
    cicle = 0

    while True:
        if n_square >= N:
            c.append(cicle)
            break
        else:
            new_weight = (n_weight + 1) * W
            new_height = (n_height + 1) * H

            if new_weight < new_height:
                side = new_weight
            else:
                side = new_height
            
            n_weight = floor(side / W)
            n_height = floor(side / H)
            n_square = n_weight * n_height
            cicle += 1

counter = Counter(c)
for key in sorted(counter.keys()):
    print(f"Кількість циклів {key}: {counter[key]}")
