from random import randint
from math import sqrt, ceil, floor

N = randint(1, 1012)
W = randint(1, 109)
H = randint(1, 109)
print(f"N= {N}, W= {W}, H= {H}")

square = N * W * H

side = ceil(sqrt(square))

n_weight = floor(side / W)
n_height = floor(side / H)

n_square = n_weight * n_height

differnce = abs(W - H)
if differnce <= 35:
    while True:
        if n_square >= N:
            print(f"Потрібна дошка з стороною: {side}")
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
else:
    def min_board_size(N, W, H):
        left, right = max(W, H), min(W, H) * N
        
        while left < right:
            mid = (left + right) // 2
            if (mid // W) * (mid // H) >= N:
                right = mid 
            else:
                left = mid + 1
        
        return left

    rezult = min_board_size(N, W, H)
    print(f"Потрібна дошка з стороною: {rezult}")
