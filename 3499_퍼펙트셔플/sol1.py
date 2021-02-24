import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N 받아오기
    N = int(input())
    # 카드들을 받아오기
    cards = list(input().split())
    # 홀수라면 중간 idx값에 +1
    if N%2:
        idx = N//2 +1
    else:
        # 아니면 그대로
        idx = N//2

    # 새로운 리스트
    new = []
    # 리스트에 번갈아가면서 넣어주기
    for i in range(N//2):
        new.append(cards[i])
        new.append(cards[i+idx])
    # 홀수라면 한번더 더해주기 (가운데값)
    if N%2:
        new.append(cards[N//2])

    print("#{} {}".format(tc, ' '.join(new)))

