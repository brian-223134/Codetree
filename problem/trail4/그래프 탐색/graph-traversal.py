import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

print(sum(visited) - 1)