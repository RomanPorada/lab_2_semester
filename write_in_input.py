from random import randint

while True:
    try:
        rows = int(input("Введіть кількість рядків матриці: "))
        break
    except ValueError:
        print("Введіть число")

while True:
    try:
        cols = int(input("Введіть кількість стовпців матриці: "))
        break
    except ValueError:
        print("Введіть число")

def generate_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [randint(0, 1) for _ in range(cols)]
        matrix.append(row)
    
    return matrix

matrix = generate_matrix(rows, cols)

with open("input.txt", "w") as f:
    for row in matrix:
        f.write(" ".join(map(str, row)) + "\n")
