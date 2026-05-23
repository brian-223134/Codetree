MOD = 10**9 + 7

s = input().strip()

allowed = [0, 1, 2, 4, 5, 7, 8]

dp_tight = [0, 0, 0]
dp_loose = [0, 0, 0]

# 아직 아무 자리도 보지 않은 상태
# 합은 0이고, N과 같은 prefix 상태
dp_tight[0] = 1

for ch in s:
    limit = int(ch)

    new_tight = [0, 0, 0]
    new_loose = [0, 0, 0]

    # 이미 N보다 작아진 상태에서는 allowed 숫자를 아무거나 붙일 수 있음
    for r in range(3):
        for d in allowed:
            nr = (r + d) % 3
            new_loose[nr] = (new_loose[nr] + dp_loose[r]) % MOD

    # 아직 N과 같은 prefix인 상태
    for r in range(3):
        for d in allowed:
            if d > limit:
                continue

            nr = (r + d) % 3

            if d == limit:
                # 여전히 N과 같은 prefix
                new_tight[nr] = (new_tight[nr] + dp_tight[r]) % MOD
            else:
                # 이번 자리에서 N보다 작아짐
                new_loose[nr] = (new_loose[nr] + dp_tight[r]) % MOD

    dp_tight = new_tight
    dp_loose = new_loose

# 박수를 치지 않는 수:
# 3,6,9가 없고, 3의 배수가 아닌 수
not_clap = (
    dp_tight[1] + dp_tight[2] +
    dp_loose[1] + dp_loose[2]
) % MOD

# N 자체도 매우 크므로 MOD로 나눈 값만 계산
n_mod = 0
for ch in s:
    n_mod = (n_mod * 10 + int(ch)) % MOD

answer = (n_mod - not_clap) % MOD

print(answer)