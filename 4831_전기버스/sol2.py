import sys
sys.stdin = open("input.txt")

T = int(input())

def bus(info_numbers,charger):
    # 각각의 정보에 접근
    K = info_numbers[0]
    N = info_numbers[1]
    M = info_numbers[2]

    # 충전기 수 자체가 부족할 경우
    if N//K >M:
        return 0

    # 충전기 정보를 표현해주기 위한 초기값
    counter = [0]*N
    # 충전기 정보를 받아와 1로 표시
    for number in charger:
        counter[number] = 1



    # 현재위치 now
    now = 0
    # 목적지 goal
    goal = N
    # 충전 횟수 count
    count = 0

    # now가 goal보다 작다면 => goal에 도작하지 않았다면
    while now < goal:
        # 다음위치 now == 현재위치 + 최대갈수 있는거리
        after = now + K
        # 다음위치가 goal에 도착하거나 넘는다면 멈추기
        if after >= goal:
            break

        # now~after 사이의 정류소 리스트 between
        between = counter[now:after + 1]
        charge = 0

        # between을 돌면서 인덱스와 값(충전소가 있다면 1) 가져오기
        for idx, i in enumerate(between):
            # 충전기가 있다면 1, 따라서 if문 통과 => between중에서 제일 마지막 충전기 위치 찾기
            if i:
                charge = idx

        # 충전기 없으면 이동 불가
        if charge == 0:
            count = 0
            break

        now += charge
        count += 1
    return count



for tc in range(1, T+1):
    # K,N,M 정보가 담긴 리스트
    info_numbers = list(map(int,input().split()))

    #충전기 정보
    charger = list(map(int, input().split()))

    # 결과
    result = bus(info_numbers,charger)
    print("#{} {}".format(tc, result))

