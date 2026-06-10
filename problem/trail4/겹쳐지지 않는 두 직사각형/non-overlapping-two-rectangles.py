n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 2차원 누적합
P = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        P[i+1][j+1] = P[i][j+1] + P[i+1][j] - P[i][j] + grid[i][j]

def rect_sum(r1, c1, r2, c2):
    return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

rects = []
for r1 in range(n):
    for r2 in range(r1, n):
        for c1 in range(m):
            for c2 in range(c1, m):
                rects.append((r1, c1, r2, c2, rect_sum(r1, c1, r2, c2)))

def overlap(a, b):
    # 행 구간과 열 구간이 모두 겹쳐야 직사각형이 겹침
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])

best = -float('inf')
for i in range(len(rects)):
    for j in range(i + 1, len(rects)):
        if not overlap(rects[i], rects[j]):
            best = max(best, rects[i][4] + rects[j][4])

print(best)