import sys
sys.stdin = open("input.txt")

T = int(input())

def turn(matrix,x,y,color):
    # 주변 8개의 모드 설정
    d = [[1, 1], [-1, -1], [1, -1], [-1, 1], [1, 0], [0, 1], [0, -1], [-1, 0]]

    # 8방면 다 돌아보자
    for i in range(8):
        dx, dy = d[i][0], d[i][1]
        cx, cy = x+dx, y+dy

        # 바꿀것들 좌표 초기값
        change = []

        # break 만나기 전까지 계속돈다
        while True:
            # 다음것이 0이라면 벽 혹은 없는것
            if matrix[cy][cx] == 0:
                break
            # 다음것이 색깔이 같다면 바꿔주자
            elif matrix[cy][cx] == color:
                for j in change:
                    matrix[j[0]][j[1]] = color
                break
            # 만약 둘다 아니라면
            else:
                # 좌표를 더해줌
                change.append([cy, cx])
                # 그리고 그다음도 봐보자
                cx += dx
                cy += dy
    return matrix


for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 플레이 정보가 담겨있는 리스트
    play = [list(map(int, input().split()))for _ in range(M)]
    # 0으로 이루어진 게임판
    matrix = [[0 for _ in range(N+2)]for _ in range(N+2)]
    # 초기 위치를 설정하기 위한 가운데 값
    c = int(N/2)
    matrix[c][c] = 2
    matrix[c+1][c+1] = 2
    matrix[c+1][c] = 1
    matrix[c][c+1] = 1
    # 플레이 횟수를 총 탐색
    for i in range(len(play)):
        # x , y 돌 색깔 받아오기
        x = play[i][0]
        y = play[i][1]
        color = play[i][2]
        # 돌 놓기
        matrix[y][x] = color
        # 색바꿔주기
        turn(matrix, x, y, color)
    white = 0
    black = 0
    for i in range(N+2):
        for j in range(N+2):
            if matrix[i][j] == 1:
                black += 1
            elif matrix[i][j] == 2:
                white += 1

    print("#{} {} {}".format(tc, black, white))

