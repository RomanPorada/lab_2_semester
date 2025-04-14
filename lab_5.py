from collections import deque

def read_input(file_name):
    with open(file_name, 'r') as f:
        matrix = [list(map(int, line. strip().split())) for line in f if line.split()]
    return matrix

def write_output(file_name, result):
    with open(file_name, 'w') as f:
        f.write(str(result) + "\n")

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

def is_safe(x, y, matrix, unsafe, visited):
    rows, cols = len(matrix), len(matrix[0])
    return (0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not unsafe[x][y] and not visited[x][y])

def bfs(matrix, unsafe):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()

    for i in range(rows):
        if matrix[i][0] == 1 and not unsafe[i][0]:
            queue.append((i, 0, 0))
            visited[i][0] = True

    while queue:
        x, y, dist = queue.popleft()

        if y == cols - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny, matrix, unsafe, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
        
    return -1

def main():
    matrix = read_input("input.txt")
    unsafe = mark_unsafe_cells(matrix)
    shortest_path_lenght = bfs(matrix, unsafe)
    write_output("output.txt", shortest_path_lenght)

if __name__ == "__main__":
    main()
