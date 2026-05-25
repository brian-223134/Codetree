def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return int(x / y)

def calc(a, o, c):
    if o not in "+-/*":
        return False

    if o == '+':
        return add(a, c)
    elif o == '-':
        return subtract(a, c)
    elif o == '*':
        return multiply(a, c)
    elif o == '/':
        if c == 0:
            return False
        return divide(a, c)


a, o, c = input().split()
a = int(a)
c = int(c)

result = calc(a, o, c)

if result is False:
    print('False')
else:
    print('%d %s %d = %d' % (a, o, c, result))