import sys
sys.stdin = open("input.txt")

T = 10

def ladder(numbers):

    # 레인지 오류 막기위해 양옆에 0으로 된 줄 생성
    for i in range(100):
        numbers[i].insert(0, 0)
        numbers[i].append(0)

    #  출발지 기준 반복문작성
    for i in range(1, 101):
        # 출발지
        sp = i

        dx = [0, -1, 1] # 하 좌 우
        dy = [1, 0, 0]

        # 현재 x,y 좌표와 방향
        cx = i
        cy = 0
        # 현재위치
        cp = numbers[cy][cx]
        d = 0

        # cp가 1인 경우만 출발
        while cp == 1:
            d = 0
            cy += dy[d]
            cx += dx[d]
            cp = numbers[cy][cx]

            if cy == 99:
                break

            moved = 0

            while numbers[cy][cx+1] == 1:
                d = 2
                cy += dy[d]
                cx += dx[d]
                cp = numbers[cy][cx]
                moved = 1

            while numbers[cy][cx-1] == 1 and moved == 0:
                d = 1
                cy += dy[d]
                cx += dx[d]
                cp = numbers[cy][cx]

        if cp == 2:
            boom = sp -1
            return boom

for tc in range(1, T+1):
    t = int(input())
    numbers = []
    for _ in range(100):
        numbers.append(list(map(int, input().split())))
    result = ladder(numbers)
    print("#{} {}".format(tc, result))

