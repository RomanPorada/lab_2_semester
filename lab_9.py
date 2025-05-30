from math import sqrt

def read(filename):
    with open(filename, "r") as f:
        w = int(f.readline().strip())
        data = list(map(int, f.readline().strip().split()))
    return w, data

def search_max_len_cable(w, heights):

    n = len(heights)


    dp = [{} for _ in range(n)]

    for h in range(1, heights[0] + 1):
        dp[0][h] = 0

    for i in range(1, n):
        for h_curr in range(1, heights[i] + 1):
            max_len = 0
            for h_prev in dp[i - 1]:
                segment = sqrt(w**2 + (h_curr - h_prev)**2)
                max_len = max(max_len, dp[i - 1][h_prev] + segment)
            dp[i][h_curr] = max_len

    max_total_length = max(dp[-1].values())

    return round(max_total_length, 2)

w, heights = read("input.txt")
print(search_max_len_cable(w, heights))
