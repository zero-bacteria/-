import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 각각 변수 받아옴
    D, H, M = map(int, input().split())
    # 날에서 빼기
    day = D - 11
    # 그대로 또 빼주기
    hour = day*24 + H - 11
    minute = hour*60 + M - 11
    # 먼저 차였다면 따흑..
    if minute < 0:
        result = -1
    # 아니라면..ㅜ
    else:
        result = minute
    print("#{} {}".format(tc, result))

