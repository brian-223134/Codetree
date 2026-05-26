def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


def is_digit_sum_even(n):
    digit_sum = 0
    
    while n > 0:
        digit_sum += n % 10
        n //= 10
    
    return digit_sum % 2 == 0


a, b = map(int, input().split())

cnt = 0

for num in range(a, b + 1):
    if is_prime(num) and is_digit_sum_even(num):
        cnt += 1

print(cnt)