import sys
sys.stdin = open("input.txt")

T = int(input())

def purple(N,numbers):
    # 같은색 영역은 겹치지 않는다는 조건이 있어서 단순히 색이 있는곳은 1을 더할예정
    # 이런 조건이 없다면 다시 고려해봐야 함

    #  배경 0으로 지정(초기값)
    #  이중 리스트 생성할때 얕은 복사를 피하기 위해서 * 으로 표현하는 것이 아닌 for 로 생성해야 한다.
    back_ground = [[0 for _ in range(10)]for _ in range(10)]

    # N개의 사각형에 대한 반복문
    for i in range(N):

        # 시작점 끝점 길이 지정(x,y 범위 지정
        x_range = range(numbers[i][0], numbers[i][2]+1)
        y_range = range(numbers[i][1], numbers[i][3]+1)

        # 좌표에 대입
        for j in x_range:
            for k in y_range:
                back_ground[j][k] = 1 + back_ground[j][k]
    # 카운트 초기값
    count = 0
    # 기존 배경에서 두개의 색이 칠해진 곳 찾기
    for i in range(10):
        for j in range(10):
            if back_ground[i][j] == 2:
                count += 1

    return count


for tc in range(1, T+1):
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(list(map(int, input().split())))
    result = purple(N, numbers)
    print("#{} {}".format(tc, result))



