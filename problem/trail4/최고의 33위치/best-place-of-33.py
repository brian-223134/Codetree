n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n - 2):
    for j in range(n - 2):
        coin_count = 0

        for x in range(i, i + 3):
            for y in range(j, j + 3):
                coin_count += grid[x][y]

        answer = max(answer, coin_count)

print(answer)