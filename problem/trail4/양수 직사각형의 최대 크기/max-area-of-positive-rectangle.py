n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_area = -1

for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                is_positive_rectangle = True
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        if grid[i][j] <= 0:
                            is_positive_rectangle = False
                            break
                    if not is_positive_rectangle:
                        break
                
                if is_positive_rectangle:
                    area = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if area > max_area:
                        max_area = area

print(max_area)