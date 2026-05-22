def has_target(i):
    temp = str(i)
    result = any(char in temp for char in "369")
    return result

def solution(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 3 == 0:
            cnt += 1
            continue
        if has_target(i):
            cnt += 1
    return cnt

a, b = map(int, input().split())

res = solution(a, b)
print(res)