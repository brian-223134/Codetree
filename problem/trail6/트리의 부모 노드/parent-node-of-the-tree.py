from collections import deque
import sys

input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    n = int(input())

    # 인접 리스트 생성 (1번 인덱스부터 사용하기 위해 n + 1 크기)
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (n + 1)

    queue = deque([1])
    parent[1] = 1 

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if parent[neighbor] == 0:
                parent[neighbor] = current 
                queue.append(neighbor)

    print("\n".join(map(str, parent[2 : n + 1])))

if __name__ == "__main__":
    solve()