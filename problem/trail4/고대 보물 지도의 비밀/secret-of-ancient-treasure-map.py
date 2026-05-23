import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

INF = -10**18

# dp[j] = 현재 위치에서 끝나고, 음수를 정확히 j개 포함하는 연속합의 최댓값
dp = [INF] * (K + 1)

answer = INF

for x in arr:
    new_dp = [INF] * (K + 1)

    if x < 0:
        # 현재 음수 하나만 선택해서 새로 시작
        if K >= 1:
            new_dp[1] = max(new_dp[1], x)

        # 기존 구간에 현재 음수를 붙임
        for j in range(1, K + 1):
            if dp[j - 1] != INF:
                new_dp[j] = max(new_dp[j], dp[j - 1] + x)

    else:
        # 현재 숫자 하나만 선택해서 새로 시작
        new_dp[0] = max(new_dp[0], x)

        # 기존 구간에 현재 숫자를 붙임
        for j in range(K + 1):
            if dp[j] != INF:
                new_dp[j] = max(new_dp[j], dp[j] + x)

    dp = new_dp

    # 음수가 K개 이하인 모든 경우 중 최댓값 갱신
    answer = max(answer, max(dp))

print(answer)