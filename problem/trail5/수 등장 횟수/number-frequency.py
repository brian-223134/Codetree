from collections import Counter
import sys

def solve():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    queries = list(map(int, input().split()))

    count_map = Counter(arr)

    result = []
    for q in queries:
        result.append(count_map[q])

    print(*(result))

if __name__ == "__main__":
    solve()