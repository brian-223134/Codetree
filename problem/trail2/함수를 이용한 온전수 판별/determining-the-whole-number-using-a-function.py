def is_sol(num):
    if num % 2 != 0 and num % 10 != 5 and not(num % 3 == 0 and num % 9 != 0):
        return True
    return False

a, b = map(int, input().split())
cnt = 0
for i in range(a,b+1):
    if(is_sol(i)):
        cnt+=1
print(cnt)