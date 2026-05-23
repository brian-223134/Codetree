n = int(input())

blue_sum = 0
diffs = []

for _ in range(2 * n):
    r, b = map(int, input().split())

    blue_sum += b
    diffs.append(r - b)

diffs.sort(reverse=True)

answer = blue_sum + sum(diffs[:n])

print(answer)