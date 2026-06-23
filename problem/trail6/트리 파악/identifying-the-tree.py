import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

graph = [[] for _ in range(n + 1)]

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

depth = [-1] * (n + 1)
depth[1] = 0

q = deque([1])
answer = 0

while q:
    cur = q.popleft()
    is_leaf = True

    for nxt in graph[cur]:
        if depth[nxt] == -1:
            depth[nxt] = depth[cur] + 1
            q.append(nxt)
            is_leaf = False

    if cur != 1 and is_leaf:
        answer += depth[cur]

print(1 if answer % 2 == 1 else 0)