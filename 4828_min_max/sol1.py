import sys
sys.stdin = open("sample_input.txt")

T = int(input())

# 필요한 함수선언
def min_max(numbers):
    # 맥스 초기값 설정
    max_value = 0
    # min 초기값 설정
    min_value = numbers[0]

    # 반복문 통해 맥스값,최소값 도출
    for number in numbers:
        if number>max_value:
            max_value = number
        if number<min_value:
            min_value = number

    #최대값과 최소값 차이
    return max_value - min_value

for tc in range(1, T+1):
    # 각 케이스 첫줄의 양수의 개수 N
    N=int(input())
    # 숫자들을 리스트로 받아옴
    numbers = list(map(int,input().split()))
    # 만들은 함수를 이용해 결과값 도출
    result = min_max(numbers)
    print("#{} {}".format(tc,result))

