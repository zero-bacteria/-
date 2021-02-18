import sys
sys.stdin = open("input.txt")

T = int(input())

def harvest(N,filed):
    # 정중앙 인덱스 값 설정
    center_idx = N//2
    # 가장 중앙의 값
    total = 0
    for i in range(N):
        total += filed[i][center_idx]

    # 왼쪽 값
    # 갈수록 y축범위가 커짐
    for i in range(center_idx):
        for j in range(center_idx-i, center_idx+i+1):
            total += filed[j][i]

    # 오른쪽 값
    # 오른쪽 출발 감소되는 방향
    # 범위 설정을 위한 임의의 값 설정
    r=-1
    for i in range(N-1, center_idx, -1):
        r += 1
        for j in range(center_idx-r, center_idx+r+1):
                total += filed[j][i]

    return total

for tc in range(1, T+1):
    N = int(input())
    filed = []
    for i in range(N):
        filed.append(list(map(int, input())))
    result = harvest(N, filed)
    print("#{} {}".format(tc, result))
