import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dfs(now, target, dist, visited):
    if now == target:
        return dist
    
    visited[now] = True
    
    for next_node, weight in graph[now]:
        if not visited[next_node]:
            result = dfs(next_node, target, dist + weight, visited)
            if result != -1:
                return result
                
    return -1

for _ in range(m):
    start, end = map(int, input().split())
    if start == end:
        print(0)
    else:
        visited = [False] * (n + 1)
        print(dfs(start, end, 0, visited))