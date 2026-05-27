m, d = map(int, input().split())

def is_valid_date(m, d):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if m < 1 or m > 12:
        return False
    
    if d < 1 or d > days[m]:
        return False
    
    return True

if is_valid_date(m, d):
    print("Yes")
else:
    print("No")