N, M = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (M) for _ in range(N)]
dp[N - 1][M - 1] = 1

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y, W, dp):
    if dp[y][x] != -1:
        return dp[y][x]

    tmp = 0
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < M and 0 <= ny < N and W[y][x] > W[ny][nx]:
            tmp += dfs(nx, ny, W, dp)
    dp[y][x] = tmp

    return dp[y][x]
print(dfs(0, 0, W, dp))