import sys
from collections import deque

m = int(sys.stdin.readline())

if m == 0:
    print(1)
    sys.exit()

edges = []
nodes = set()
in_degree = {}
adj = {}

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))
    nodes.add(u)
    nodes.add(v)
    
    if u not in adj:
        adj[u] = []
    adj[u].append(v)
    
    in_degree[v] = in_degree.get(v, 0) + 1
    if u not in in_degree:
        in_degree[u] = 0

root = None
root_count = 0
is_tree = True

for node in nodes:
    deg = in_degree.get(node, 0)
    if deg == 0:
        root = node
        root_count += 1
    elif deg > 1:
        is_tree = False
        break

if root_count != 1:
    is_tree = False

if is_tree:
    visited = set()
    queue = deque([root])
    visited.add(root)
    
    while queue:
        curr = queue.popleft()
        if curr in adj:
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    if len(visited) != len(nodes):
        is_tree = False

if is_tree:
    print(1)
else:
    print(0)