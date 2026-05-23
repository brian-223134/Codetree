n, m = map(int, input().split())
arr = list(map(int, input().split()))

OFFSET = 20
LIMIT = 40

dp = [0] * 41
dp[OFFSET] = 1   # 아직 아무 숫자도 쓰지 않았을 때 합은 0

for x in arr:
    new_dp = [0] * 41

    for idx in range(41):
        if dp[idx] == 0:
            continue

        current_sum = idx - OFFSET

        plus_sum = current_sum + x
        minus_sum = current_sum - x

        if -20 <= plus_sum <= 20:
            new_dp[plus_sum + OFFSET] += dp[idx]

        if -20 <= minus_sum <= 20:
            new_dp[minus_sum + OFFSET] += dp[idx]

    dp = new_dp

print(dp[m + OFFSET])