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

    # 충전기가 필요한 범위설정 반복
    for i in range(N-K):
        check = 0
        # K번안에 충전기 있는지 탐색
        for j in (range(i,i+K)):
            if counter[j] == 1 :
                check += 1

        if check == 0:
            return 0

    return N//K



for tc in range(1, T+1):
    # K,N,M 정보가 담긴 리스트
    info_numbers = list(map(int,input().split()))

    #충전기 정보
    charger = list(map(int, input().split()))

    # 결과
    result = bus(info_numbers,charger)
    print("#{} {}".format(tc, result))

