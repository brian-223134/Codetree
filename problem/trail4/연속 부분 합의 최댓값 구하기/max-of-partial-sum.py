n = int(input())
arr = list(map(int, input().split()))

# dp[i]는 i번째 원소를 마지막으로 포함하는 연속 합의 최댓값
dp = [0] * n

# 0번째 인덱스 초기화 (문제 조건에 따라 2 * arr[0] 또는 arr[0])
dp[0] = arr[0] 

for i in range(1, n):
    # 이전까지의 최적의 합에 현재 값을 더할지, 아니면 현재 값부터 새로 시작할지 결정
    dp[i] = max(dp[i-1] + arr[i], arr[i])

# 전체 dp 테이블 중 가장 큰 값이 정답
print(max(dp))
