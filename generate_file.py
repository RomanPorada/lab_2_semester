import csv
import random

def generate_wells_csv(filename, num_wells=10, min_distance=100, max_distance=5000, extra_edges=5, connected=True):
    wells = [f"K{i+1}" for i in range(num_wells)]
    edges = set()

    if connected:
        for i in range(1, num_wells):
            k1 = wells[i]
            k2 = wells[random.randint(0, i - 1)]
            dist = random.randint(min_distance, max_distance)
            edge = tuple(sorted((k1, k2))) + (dist,)
            edges.add(edge)

        while len(edges) < (num_wells - 1 + extra_edges):
            k1, k2 = random.sample(wells, 2)
            if k1 != k2:
                dist = random.randint(min_distance, max_distance)
                edge = tuple(sorted((k1, k2))) + (dist,)
                edges.add(edge)
    else:
        while len(edges) < extra_edges:
            k1, k2 = random.sample(wells, 2)
            if k1 != k2:
                dist = random.randint(min_distance, max_distance)
                edge = tuple(sorted((k1, k2))) + (dist,)
                edges.add(edge)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for k1, k2, dist in edges:
            writer.writerow([k1, k2, dist])

randomm = random.randint(0, 1)
if randomm == 0:
    conected = False
else:
    conected = True
wells = int(input("Введіть кількість колодязів: "))
min_distance = int(input("Введіть мінімальну відстань між колодязями: "))
max_distance = int(input("Введіть максимальну відстань між колодязями: "))
generate_wells_csv('communication_wells.csv', wells, min_distance, max_distance, extra_edges=4, connected= conected)
