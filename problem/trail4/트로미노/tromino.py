n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 1. ㄴ자 블록
# 2x2 영역에서 한 칸을 제외한 3칸을 선택
for i in range(n - 1):
    for j in range(m - 1):
        total = (
            grid[i][j] +
            grid[i + 1][j] +
            grid[i][j + 1] +
            grid[i + 1][j + 1]
        )
        min_value = min(
            grid[i][j],
            grid[i + 1][j],
            grid[i][j + 1],
            grid[i + 1][j + 1]
        )
        ans = max(ans, total - min_value)

# 2. 가로 일자 블록
for i in range(n):
    for j in range(m - 2):
        total = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        ans = max(ans, total)

# 3. 세로 일자 블록
for i in range(n - 2):
    for j in range(m):
        total = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
        ans = max(ans, total)

print(ans)