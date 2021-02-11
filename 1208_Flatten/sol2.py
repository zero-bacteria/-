import sys
sys.stdin = open("input.txt")

T = 10

def flatten(N,numbers):

    # while로 실행
    while N >-1 :
        # 각각의 값 초기화
        max_value = 0
        min_value = 100
        max_idx = 0
        min_idx = 0
        # 최대 최소값 찾기
        for i in range(len(numbers)):
            if numbers[i]>=max_value:
                max_value = numbers[i]
                max_idx = i
            if numbers[i]<=min_value:
                min_value = numbers[i]
                min_idx = i
        # 차이 저장
        gap = max_value - min_value
        # 평탄화 시작
        numbers[max_idx] = numbers[max_idx] - 1
        numbers[min_idx] = numbers[min_idx] + 1

        # 횟수 1회 감소
        N -= 1

    return gap




for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    result = flatten(N,numbers)
    print("#{} {}".format(tc,result))

