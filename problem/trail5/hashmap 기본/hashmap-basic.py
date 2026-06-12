import sys

def solve():
    input = sys.stdin.readline

    n = int(input())

    hashmap = {}

    for _ in range(n):
        line = input().split()
        cmd = line[0]
        k = int(line[1])

        if cmd == "add":
            v = int(line[2])
            hashmap[k] = v

        elif cmd == "remove":
            hashmap.pop(k, None)

        elif cmd == "find":
            if k in hashmap:
                print(hashmap[k])
            else:
                print("None")


if __name__ == "__main__":
    solve()