from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def can_go(y, x):
    return in_range(y, x) and not visited[y][x] and grid[y][x] == 0


q = deque()

# 모든 시작점을 큐에 먼저 넣는다
for r, c in points:
    y, x = r - 1, c - 1   # 1-indexed -> 0-indexed

    if not visited[y][x]:
        visited[y][x] = True
        q.append((y, x))

answer = 0

while q:
    y, x = q.popleft()
    answer += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if can_go(ny, nx):
            visited[ny][nx] = True
            q.append((ny, nx))

print(answer)