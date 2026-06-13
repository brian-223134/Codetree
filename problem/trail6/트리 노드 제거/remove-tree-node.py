import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    parent_list = list(map(int, input().split()))
    remove_node = int(input())

    root = -1
    tree = [[] for _ in range(n)]

    for child in range(n):
        parent = parent_list[child]
        if parent == -1:
            root = child
        else:
            if child != remove_node:
                tree[parent].append(child)

    if root == remove_node:
        print(0)
        return

    leaf_count = 0

    def dfs(current):
        nonlocal leaf_count

        if not tree[current]:
            leaf_count += 1
            return

        for next_node in tree[current]:
            dfs(next_node)

    dfs(root)

    print(leaf_count)

if __name__ == "__main__":
    solve()