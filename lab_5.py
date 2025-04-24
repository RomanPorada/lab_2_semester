from collections import deque

def read_input(file_name):
    with open(file_name, 'r') as f:
        matrix = [list(map(int, line. strip().split())) for line in f if line.split()]
    return matrix

def write_output(file_name, result):
    distance, path = result
    with open(file_name, 'w') as f:
        if distance == -1:
            f.write("-1\n")
        else:
            f.write(f"{distance}\n")
            for step in path:
                f.write(f"{step}\n")
        

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def mark_unsafe_cells(matrix):
    rows, cols = len(matrix), len(matrix[0])
    unsafe = [[False]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                unsafe[i][j] = True
                for d in range(8):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < rows and 0 <= nj < cols:
                        unsafe[ni][nj] = True

    return unsafe

def build_graph(matrix, unsafe):
    rows, cols = len(matrix), len(matrix[0])
    graph = {}

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 1 and not unsafe[x][y]:
                neighbors = []
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1 and not unsafe[nx][ny]):
                        neighbors.append((nx, ny))

                graph[(x, y)] = neighbors
    
    return graph

def bfs(graph, matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    queue = deque()
    parent = {}

    for i in range(rows):
        if matrix[i][0] == 1 and (i, 0) in graph:
            queue.append(((i, 0), 0))
            visited.add((i, 0))
            parent[(i, 0)] = None

    while queue:
        (x, y), dist = queue.popleft()

        if y == cols -1:
            path = []
            node = (x, y)
            while node:
                path.append(node)
                node = parent[node]
            path.reverse()
            return dist, path
        
        for neighbor in graph.get((x, y), []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = (x, y)
                queue.append((neighbor, dist + 1))

    return -1, []

def main():
    matrix = read_input("input.txt")
    unsafe = mark_unsafe_cells(matrix)
    graph = build_graph(matrix, unsafe)
    result = bfs(graph, matrix)
    write_output("output.txt", result)

if __name__ == "__main__":
    main()
