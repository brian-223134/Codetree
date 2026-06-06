n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_happy(arr):
    count = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1

        if count >= m:
            return True

    return m == 1

answer = 0

# 행 검사
for i in range(n):
    if is_happy(grid[i]):
        answer += 1

# 열 검사
for j in range(n):
    col = []
    for i in range(n):
        col.append(grid[i][j])

    if is_happy(col):
        answer += 1

print(answer)