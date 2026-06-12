from collections import Counter
import sys

def solve():
    input = sys.stdin.readline

    n = int(input())

    words = [input().strip() for _ in range(n)]

    word_counts = Counter(words)

    max_count = max(word_counts.values()) if word_counts else 0

    print(max_count)

if __name__ == "__main__":
    solve()