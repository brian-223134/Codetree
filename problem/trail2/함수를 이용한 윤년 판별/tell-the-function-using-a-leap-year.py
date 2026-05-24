def sol(num):
    if num % 4 == 0:
        if num % 100 == 0 and num % 400 != 0:
            return False
        else:
            return True
    return False

y = int(input())

if sol(y):
    print("true")
else:
    print("false")