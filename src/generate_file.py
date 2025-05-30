import random

def generate():
    w = random.randint(1, 100)
    n = random.randint(1, 50)

    all_heights = []

    for _ in range(n):
        height = random.randint(1, 100)
        all_heights.append(f"{height}")

    with open("input.txt", 'w') as f:
        f.write(f"{w} \n")
        f.write(' '.join(all_heights) + "\n")
    
    print("Файл згенеровано успішно")

if __name__ == "__main__":
    generate()