N = int(input())

arr = []

for _ in range(N):
    line = input().split()
    cmd = line[0]

    if cmd == "push_back":
        x = int(line[1])
        arr.append(x)

    elif cmd == "pop_back":
        arr.pop()

    elif cmd == "size":
        print(len(arr))

    elif cmd == "get":
        k = int(line[1])
        print(arr[k - 1])