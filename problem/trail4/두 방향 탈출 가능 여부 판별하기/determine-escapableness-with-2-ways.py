n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 아래, 오른쪽
dirs = [(1, 0), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and grid[x][y] == 1 and not visited[x][y]

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            dfs(nx, ny)

dfs(0, 0)

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)