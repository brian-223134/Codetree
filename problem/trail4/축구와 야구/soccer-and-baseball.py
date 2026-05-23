n = int(input())

students = []
for _ in range(n):
    si, bi = map(int, input().split())
    students.append((si, bi))

NEG = -10**18

dp = [[NEG] * 10 for _ in range(12)]
dp[0][0] = 0

for si, bi in students:
    new_dp = [row[:] for row in dp]

    for soccer in range(12):
        for baseball in range(10):
            if dp[soccer][baseball] == NEG:
                continue

            # 현재 학생을 축구팀에 넣는 경우
            if soccer + 1 <= 11:
                new_dp[soccer + 1][baseball] = max(
                    new_dp[soccer + 1][baseball],
                    dp[soccer][baseball] + si
                )

            # 현재 학생을 야구팀에 넣는 경우
            if baseball + 1 <= 9:
                new_dp[soccer][baseball + 1] = max(
                    new_dp[soccer][baseball + 1],
                    dp[soccer][baseball] + bi
                )

    dp = new_dp

print(dp[11][9])