import random

def generate_input():
    n = int(input("Введіть кількість працівників (N): "))
    b = int(input("Введіть кількість сортів пива (B): "))

    all_preferences = []

    for _ in range(n):
        row = ['N'] * b
        liked_indices = random.sample(range(b), random.randint(1, b))  # мінімум одне пиво
        for i in liked_indices:
            row[i] = 'Y'
        all_preferences.append(''.join(row))

    with open("input.txt", "w") as f:
        f.write(f"{n} {b}\n")
        f.write(' '.join(all_preferences) + "\n")

    print("Файл input.txt успішно згенеровано!")

if __name__ == "__main__":
    generate_input()
