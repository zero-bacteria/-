import sys
sys.stdin = open("input.txt")

T = int(input())

def sell(N,M,K, arrival_info):
    # 일단 손님 시간순으로 정렬
    for i in range(len(arrival_info)-1,0,-1):
        for j in range(0,i):
            if arrival_info[j] > arrival_info[j+1]:
                arrival_info[j], arrival_info[j+1] = arrival_info[j+1], arrival_info[j]
    # 현재 붕어빵 수
    cnt = - K

    # 최대시간만큼 흘러갔을때
    for i in range(0, arrival_info[-1]+1):
        # 붕어빵나오는 시간이면
        # 즉 붕어빵나오는 시간으로 나누었을때 나머지가 없으면
        if not i % M:
            # 붕어빵 생성
            cnt += K
        # 손님이 오는 시각하고 일치하는지 검사하기 위해 반복문돌림
        for j in arrival_info:
            # 일치한다면
            if i == j:
                cnt -= 1
        if cnt < 0:
            return 'Impossible'

    return 'Possible'

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrival_info = list(map(int, input().split()))
    result = sell(N, M, K, arrival_info)
    print("#{} {}".format(tc, result))

