n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

answer = 0

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 시작점은 아래쪽 꼭짓점
for r in range(n):
    for c in range(n):

        # a: 1번/3번 방향으로 이동할 길이
        # b: 2번/4번 방향으로 이동할 길이
        for a in range(1, n):
            for b in range(1, n):

                cur_r, cur_c = r, c
                total = grid[cur_r][cur_c]
                possible = True

                lengths = [a, b, a, b]

                for d in range(4):
                    for step in range(lengths[d]):
                        cur_r += dr[d]
                        cur_c += dc[d]

                        if not in_range(cur_r, cur_c):
                            possible = False
                            break

                        # 마지막에 시작점으로 돌아오는 칸은 중복으로 더하지 않음
                        if not (d == 3 and step == lengths[d] - 1):
                            total += grid[cur_r][cur_c]

                    if not possible:
                        break

                if possible and cur_r == r and cur_c == c:
                    answer = max(answer, total)

print(answer)