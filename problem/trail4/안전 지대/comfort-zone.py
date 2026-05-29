from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_height = max(max(row) for row in grid)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy, k, visited):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] > k:
                    visited[nx][ny] = True
                    q.append((nx, ny))


best_k = 1
max_safe_area = 0

for k in range(1, max_height + 1):
    visited = [[False] * m for _ in range(n)]
    safe_area_count = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > k:
                bfs(i, j, k, visited)
                safe_area_count += 1

    if safe_area_count > max_safe_area:
        max_safe_area = safe_area_count
        best_k = k

print(best_k, max_safe_area)