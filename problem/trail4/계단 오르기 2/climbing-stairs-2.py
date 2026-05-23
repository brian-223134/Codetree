import sys

input = sys.stdin.readline

N = int(input())
coins = [0] + list(map(int, input().split()))

INF = -10**18

# dp[i][k] = i층까지 올라왔고, 1계단 이동을 k번 사용했을 때 최대 동전 수
dp = [[INF] * 4 for _ in range(N + 1)]

# 0층, 즉 시작 지점
dp[0][0] = 0

for i in range(1, N + 1):
    for k in range(4):
        # 2계단 올라오는 경우
        if i - 2 >= 0:
            dp[i][k] = max(dp[i][k], dp[i - 2][k] + coins[i])

        # 1계단 올라오는 경우
        if i - 1 >= 0 and k >= 1:
            dp[i][k] = max(dp[i][k], dp[i - 1][k - 1] + coins[i])

print(max(dp[N]))