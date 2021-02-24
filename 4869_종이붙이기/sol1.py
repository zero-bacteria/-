import sys
sys.stdin = open("input.txt")

T = int(input())

def tape(N):
    # 만약 N의 길이가 20이라면 3가지 방법밖에 없음
    if N == 20:
        return 3
    # 만약 10이 남았다면 남은 경우의 수는 1가지 밖에 없음
    elif N == 10:
        return 1
    # 아니라면 세로가 왔을때와 가로가 왔을때 두가지 경우가 생김
    # 하지만 가로의 경우 2가지가 생김
    return tape(N-10) + 2*tape(N-20)

for tc in range(1, T+1):
    N = int(input())
    result = tape(N)
    print("#{} {}".format(tc, result))

