import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    if N%2:
        idx = N//2 +1
    else:
        idx = N//2

    new = []
    for i in range(N//2):
        new.append(cards[i])
        new.append(cards[i+idx])

    if N%2:
        new.append(cards[N//2])

    print("#{} {}".format(tc, ' '.join(new)))

