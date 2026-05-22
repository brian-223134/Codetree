n = int(input())

if n % 2 == 0:
    temp = 0
    while(1):
        temp += n % 10
        n = n // 10
        if (n == 0):
            break
    if temp % 5 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')
