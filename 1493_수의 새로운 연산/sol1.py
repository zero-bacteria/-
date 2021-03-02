import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    p, q = map(int, input().split())

    # x축 값이 증가 할수록 2,3,4이런식으로 커짐
    # y축이 감소할수록 1,2,3,4 이런 방식으로 커짐
    # x축 값 설정

    x = []
    i = 0
    # 최대값이 10000
    while i <= 50000:
        # j값이 점점 커짐에따라 커지는 x축의 값
        # j범위는 그냥 무작위로 잡음
        # 0번인덱스에 0의 값을추가해 혼동 방지
        for j in range(0, 50000):
            i = i+j
            x.append(i)

    # x값의 어느범위에 위치해있는가 파악
    for i in range(len(x)):
        if p <= x[i]:
            px = i
        if q <= x[i]:
            qx = i

    # x범위를 기준으로 실제 수에서 뺀만큼을 구해서 x,y 좌표를 대입시킬 수 있음
    dp = x[px] - p
    dq = x[qx] - q

    # 단순 계산 과정을 위한 코드들
    point_P = (px - dp, dp+1)
    point_Q = (qx - dq, dq+1)
    nx = px-dp+qx-dq
    ny = dp+dq+2

    new_point = (nx, ny)
    result = x[nx-1]
    for i in range(ny-1):
        result += nx+i

    print("#{} {}".format(tc, result))

