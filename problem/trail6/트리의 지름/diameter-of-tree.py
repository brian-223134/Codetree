from collections import deque
import sys

input = sys.stdin.readline

def solve():
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    def bfs(start_node):
        distances = [-1] * (n + 1)
        queue = deque([start_node])
        distances[start_node] = 0

        max_distance = 0
        farthest_node = start_node

        while queue:
            current = queue.popleft()

            for neighbor, weight in graph[current]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + weight
                    queue.append(neighbor)

                    # 가장 먼 노드 정보 갱신
                    if distances[neighbor] > max_distance:
                        max_distance = distances[neighbor]
                        farthest_node = neighbor

        return farthest_node, max_distance

    node_A, _ = bfs(1)

    _, diameter = bfs(node_A)

    print(diameter)

if __name__ == "__main__":
    solve()