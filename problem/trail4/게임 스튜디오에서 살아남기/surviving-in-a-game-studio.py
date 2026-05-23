MOD = 10**9 + 7

n = int(input())

dp = [[0] * 3 for _ in range(3)]

# 아직 아무 평가도 받지 않은 상태
# T 개수 = 0, 연속 B 개수 = 0
dp[0][0] = 1

for _ in range(n):
    new_dp = [[0] * 3 for _ in range(3)]

    for t in range(3):
        for b in range(3):
            count = dp[t][b]

            if count == 0:
                continue

            # G를 선택하는 경우
            new_dp[t][0] = (new_dp[t][0] + count) % MOD

            # B를 선택하는 경우
            if b + 1 < 3:
                new_dp[t][b + 1] = (new_dp[t][b + 1] + count) % MOD

            # T를 선택하는 경우
            if t + 1 < 3:
                new_dp[t + 1][0] = (new_dp[t + 1][0] + count) % MOD

    dp = new_dp

answer = 0

for t in range(3):
    for b in range(3):
        answer = (answer + dp[t][b]) % MOD

print(answer)