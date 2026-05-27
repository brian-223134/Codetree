n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def is_same_from(start):
    for i in range(n2):
        if a[start + i] != b[i]:
            return False
    return True


def is_continuous_subsequence():
    # B의 길이가 A보다 길면 절대 불가능
    if n2 > n1:
        return False

    # B가 A에서 시작할 수 있는 위치는 0부터 n1 - n2까지
    for start in range(n1 - n2 + 1):
        if is_same_from(start):
            return True

    return False


if is_continuous_subsequence():
    print("Yes")
else:
    print("No")