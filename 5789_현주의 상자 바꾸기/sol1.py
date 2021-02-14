import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N,Q를 받아오기 위한 리스트 만들기
    info = list(map(int, input().split()))
    # N,Q를 받아옴
    N = info[0]
    Q = info[1]

    # i번째 작업의 정보를 받아오기 위한 리스트 초기값
    numbers = []
    # 각각의 LR 값이 담긴 i번째 실행 정보 리스트 받아오기
    for i in range(Q):
        numbers.append(list(map(int, input().split())))

    # 결과 리스트 선언
    result = [0] * N

    # Q의 범위내에서 반복문작성
    for i in range(Q):
        # i번째 작업에서 L과 R사이의 박스의 범위 탐색
        for j in range(numbers[i][0],numbers[i][1]+1):
            # 해당 범위에서 L과 R 사이의 박스는 숫자 i가 들어가야하는데 i는 인덱스이므로 +1을 해준다
            # 인덱스는 0부터 시작이지만 실질적으로는 1부터시작하는 작업 순서
            # 그반대로 j에서는 -1을 해주어야 인덱스 접근이 가능하다.
            result[j-1] = i +1

    result = " ".join(map(str, result))
    print("#{} {}".format(tc, result ))

