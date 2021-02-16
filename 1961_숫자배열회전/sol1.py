import sys
sys.stdin = open("input.txt")

T = int(input())



def arr_rotate(numbers):
    # 초기값 생성
    rot_numbers = [[0 for _ in range(N)] for _ in range(N)]
    # 배열에 접근
    for i in range(N):
        for j in range(N):
            # 시계방향은 x,y가 바뀌고 다음과 같은 규칙을 가지게 됨
            rot_numbers[j][N-1-i] = numbers[i][j]
    return rot_numbers

for tc in range(1, T+1):
    N = int(input())
    numbers = []
    for i in range(N):
        numbers.append(list(map(int,input().split())))
    # 각각의 각도별로 생성
    rot_90 = arr_rotate(numbers)
    rot_180 = arr_rotate(rot_90)
    rot_270 = arr_rotate(rot_180)

    #  원하는 출력을 위해 반복문 사용
    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, rot_90[i])), ''.join(map(str, rot_180[i])), ''.join(map(str, rot_270[i])))


