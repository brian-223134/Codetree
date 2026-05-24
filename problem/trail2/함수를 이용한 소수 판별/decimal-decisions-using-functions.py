import math

# 2 ~ int(sqrt(num))까지 중에서 나눠떨어지지 않으면 소수
def is_prime(num):
    s = int(math.sqrt(num))
    for i in range(2,s + 1):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())

res = 0
for i in range(a, b + 1):
    if(is_prime(i)):
        res += i

print(res)