n, m = map(int, input().split())
arr = list(map(int, input().split()))

NEG = -10**15

not_sel = [NEG] * (m + 1)
in_sel = [NEG] * (m + 1)

# 아직 아무 숫자도 보지 않았고, 구간도 0개 고른 상태
not_sel[0] = 0

for x in arr:
    new_not = [NEG] * (m + 1)
    new_in = [NEG] * (m + 1)

    for j in range(m + 1):
        # 현재 숫자를 선택하지 않는 경우
        new_not[j] = max(not_sel[j], in_sel[j])

        # 현재 숫자를 기존 구간에 이어 붙이는 경우
        if in_sel[j] != NEG:
            new_in[j] = max(new_in[j], in_sel[j] + x)

        # 현재 숫자에서 새 구간을 시작하는 경우
        if j + 1 <= m and not_sel[j] != NEG:
            new_in[j + 1] = max(new_in[j + 1], not_sel[j] + x)

    not_sel = new_not
    in_sel = new_in

print(max(not_sel[m], in_sel[m]))