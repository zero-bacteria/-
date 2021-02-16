import sys
sys.stdin = open("input.txt")

T = int(input())

def snail(N):
    numbers = [[0 for _ in range(N)]for _ in range(N)]
    dx = [1, 0, -1, 0]  # x축 좌표 시계방향 순서에 따라 우 하 좌 상
    dy = [0, 1, 0, -1]  # y축 좌표 시계방향 순서에 따라
    # 현재 x,y 위치와 방향 d 초기값
    cx = 0
    cy = 0
    d = 0

    # 숫자 입력
    for i in range(0, N*N):
        # N을 입력
        numbers[cy][cx] = i+1
        # 현재 방향 전환
        cx += dx[d]
        cy += dy[d]
        # 지정 범위내에 존재하지 않거나 이미 지정한 값이 있다면
        if not 0 <= cx <= N-1 or not 0 <= cy <= N-1 or numbers[cy][cx]:
            # 실행취소
            cx -= dx[d]
            cy -= dy[d]
            # 방향전환
            d = (d+1) % 4
            # 다시가
            cx += dx[d]
            cy += dy[d]

    return numbers


for tc in range(1, T+1):
    N = int(input())
    result = '\n'.join([' '.join(map(str, row)) for row in snail(N)])
    print('#{}'.format(tc))
    print('{}'.format(result))

