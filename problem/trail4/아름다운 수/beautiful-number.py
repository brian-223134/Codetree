n = int(input())

dp = [0] * (n + 1)
dp[0] = 1  # 아무것도 안 붙인 상태 1가지

for i in range(1, n + 1):
    for d in range(1, 5):  # 마지막에 붙인 블록: 1, 22, 333, 4444
        if i >= d:
            dp[i] += dp[i - d]

print(dp[n])