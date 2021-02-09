import sys
sys.stdin = open("input.txt")

T = int(input())

def range_sum(info,numbers):
    # 정수의 개수 N
    N = info[0]
    # 구간의 개수 M
    M = info[1]

    # 맥스 초기값 선언
    max_value = 0
    # min 초기값 선언(1)
    min_value = 0
    # min 값을 추정하기 힘들어 초기 M구간의 합을 최솟값으로 지정
    for i in range(M):
        min_value += numbers[i]

    # 구간합을 실행하기 위해 전체길에서 (M-1)만큼을 제외한 값을 지정(index 넘지 않기 위해)
    for i in range(len(numbers)-M+1):
        # 임시적인 구간합 설정
        r_sum = 0
        # M구간의 합 구하기
        for j in range(M):
            r_sum += numbers[i+j]
        # 최대값 찾기
        if r_sum>max_value:
            max_value = r_sum
        # 최소값 찾기
        if r_sum<min_value:
            min_value = r_sum

    return max_value - min_value



for tc in range(1, T+1):
    info = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = range_sum(info, numbers)
    print("#{} {}".format(tc,result ))

