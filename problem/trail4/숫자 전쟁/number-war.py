import sys

input = sys.stdin.readline

N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

INF = -10**18

# dp[i][j] = first의 i번째 카드, second의 j번째 카드를 보고 있을 때 남우가 얻을 수 있는 최대 점수
dp = [[INF] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N + 1):
    for j in range(N + 1):
        if dp[i][j] == INF:
            continue

        # 한쪽 카드 더미가 비면 게임 종료
        if i == N or j == N:
            continue

        a = first[i]
        b = second[j]

        # 1. 카드 버리기: 둘 다 버림
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

        # 2. 카드 대결
        if b < a:
            # 남우 카드가 더 작으므로 남우가 b점 획득, 남우 카드만 버림
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + b)
        elif a < b:
            # 상대 카드가 더 작으므로 상대 카드만 버림, 남우 점수 없음
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        else:
            # 같으면 둘 다 버림
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

answer = 0

# 게임은 한쪽 더미가 비면 종료되므로
# i == N 또는 j == N인 모든 상태 중 최댓값을 보면 됨
for i in range(N + 1):
    answer = max(answer, dp[i][N])

for j in range(N + 1):
    answer = max(answer, dp[N][j])

print(answer)