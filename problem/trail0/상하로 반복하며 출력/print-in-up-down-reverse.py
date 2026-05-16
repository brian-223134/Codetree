n = int(input())

for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        if j % 2 != 0:
            row.append(str(i))         
        else:
            row.append(str(n - i + 1))
    print("".join(row))
