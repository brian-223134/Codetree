import sys
sys.setrecursionlimit(100000)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
villages = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def OOB(y, x):
    return y < 0 or y >= n or x < 0 or x >= n

def dfs(y, x):
    visited[y][x] = True
    count = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if OOB(ny, nx):
            continue

        if grid[ny][nx] == 1 and not visited[ny][nx]:
            count += dfs(ny, nx)

    return count

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1 and not visited[y][x]:
            village_size = dfs(y, x)
            villages.append(village_size)

villages.sort()

print(len(villages))
for size in villages:
    print(size)