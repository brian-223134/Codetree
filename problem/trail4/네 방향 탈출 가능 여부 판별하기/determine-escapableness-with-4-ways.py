from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

def OOB(y, x):
    return y < 0 or y >= n or x < 0 or x >= m

q = deque()

q.append((0, 0))
visited[0][0] = True

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if OOB(ny, nx):
            continue

        if visited[ny][nx]:
            continue

        if a[ny][nx] == 0:
            continue

        visited[ny][nx] = True
        q.append((ny, nx))

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)