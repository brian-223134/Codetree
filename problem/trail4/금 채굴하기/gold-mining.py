n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_cost(k):
    return k * k + (k + 1) * (k + 1)

def count_gold(r, c, k):
    cnt = 0

    for i in range(n):
        for j in range(n):
            if abs(i - r) + abs(j - c) <= k:
                cnt += grid[i][j]

    return cnt

answer = 0

# K는 최대 2n - 2까지만 보면 충분
for r in range(n):
    for c in range(n):
        for k in range(2 * n):
            gold_count = count_gold(r, c, k)
            revenue = gold_count * m
            cost = get_cost(k)

            if revenue >= cost:
                answer = max(answer, gold_count)

print(answer)