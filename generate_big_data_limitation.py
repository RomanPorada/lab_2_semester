import random
import numpy as np
import gzip     
from tqdm import tqdm

def generate_input(filename, num_employees, num_beers, like_prob=0.0005):
    with gzip.open(filename, "wt") as f:
        f.write(f"{num_employees} {num_beers}\n")
        for _ in tqdm(range(num_employees), desc="Генеруємо вподобання працівників"):
            row = np.random.choice(['N', 'Y'], size=num_beers, p=[1-like_prob, like_prob])

            if 'Y' not in row:
                random_index = np.random.randint(0, num_beers)
                row[random_index] = 'Y'

            f.write(''.join(row) + " ")

if __name__ == "__main__":
    num_employees = int(input("Введіть кількість працівників (N): "))
    num_beers = int(input("Введіть кількість сортів пива (B): "))
    filename = "input.txt.gz"

    generate_input(filename, num_employees, num_beers)