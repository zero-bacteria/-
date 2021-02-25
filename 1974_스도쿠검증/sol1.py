import sys
sys.stdin = open("input.txt")

T = int(input())

def check(numbers):
    # 가로 세로 검증
    for i in range(9):
        # 합 초기화
        total = 0
        # 가로와 세로 각각 검증하기 위함
        for j in range(9):
            total += numbers[i][j]
            total += numbers[j][i]
        # 1부터 9까지 중복없이 있으면 합이 45 가로세로 두경우에 90
        if total != 90:
            return 0
    # 3x3 검증
    # 0부터 3단위로 반복
    for i in range(0,7,3):
        for j in range(0,7,3):
            total = 0
            # 해당 범위 합
            for k in range(3):
                for l in range(3):
                    total += numbers[i+k][j+l]
            if total != 45:
                return 0

    return 1

for tc in range(1, T+1):
    numbers = [list(map(int,input().split())) for _ in range(9)]
    result = check(numbers)
    print("#{} {}".format(tc, result))

