from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    num = grid[x][y]
    size = 1

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny]:
                continue

            if grid[nx][ny] != num:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))
            size += 1

    return size


bomb_count = 0
max_block_size = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_size = bfs(i, j)

            max_block_size = max(max_block_size, block_size)

            if block_size >= 4:
                bomb_count += 1

print(bomb_count, max_block_size)