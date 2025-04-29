import random
import numpy as np
import gzip     
from tqdm import tqdm

def generate_input_without_like_prob(filename, num_employees, num_beers):
    with gzip.open(filename, "wt") as f:
        f.write(f"{num_employees} {num_beers}\n")
        for _ in tqdm(range(num_employees), desc="Генеруємо вподобання працівників"):
            row = ['N'] * num_beers
            liked_count = random.randint(1, num_beers)
            liked_indices = random.sample(range(num_beers), liked_count)
            for idx in liked_indices:
                row[idx] = 'Y'
            f.write(''.join(row) + " ")

if __name__ == "__main__":
    num_employees = int(input("Введіть кількість працівників (N): "))
    num_beers = int(input("Введіть кількість сортів пива (B): "))
    filename = "input.txt.gz"

    generate_input_without_like_prob(filename, num_employees, num_beers)
