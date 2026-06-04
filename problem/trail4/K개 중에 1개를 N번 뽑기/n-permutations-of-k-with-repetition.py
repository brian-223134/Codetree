K, N = map(int, input().split())

answer = []

def choose(cnt):
    if cnt == N:
        print(*answer)
        return

    for i in range(1, K + 1):
        answer.append(i)
        choose(cnt + 1)
        answer.pop()

choose(0)