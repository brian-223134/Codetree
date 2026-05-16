n = int(input())

for i in range(1, n + 1):
    arr = []
    for j in range(1, n + 1):
        arr.append(str(j))
        
    if i % 2 == 0:
        arr.reverse()
        
    print("".join(arr))
