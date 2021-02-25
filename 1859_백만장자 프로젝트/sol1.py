import sys
sys.stdin = open("input.txt")

T = int(input())
# 매도 타이밍을 잡는 함수
def sell_point(price, start_idx):
    # 초기 고점은 시작 포인트로 잡자
    max_price = price[start_idx]
    # 고점이 오는 날짜 역시 시작 날짜
    max_idx = start_idx
    # 이익은 일단 0
    total = 0
    # price를 검토해서 최대값 생성
    for i in range(start_idx, len(price)):
        if price[i] > max_price:
            max_price = price[i]
            max_idx = i
    # 고점까지 매일 1씩 산 이득을 계산
    for i in range(start_idx, max_idx):
        total += max_price - price[i]
    # 만약 장이 마감됐다면, 즉 시작점이 끝점까지 왔다면
    if start_idx == len(price)-1:
        # 이제 끝
        return 0
    # 내가 고점에서 물리게 될거라면
    if max_idx == start_idx:
        # 하루 쉬자, 즉 한칸 넘어가자
        return sell_point(price, max_idx+1)
    # 최고점까지의 이득을 챙기고 그다음 고점 검토를 해보자
    return sell_point(price, max_idx) + total

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    result = sell_point(price,0)
    print("#{} {}".format(tc, result))

