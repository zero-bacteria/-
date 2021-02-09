import sys
sys.stdin = open("input.txt")

T = int(input())

def max_card(N,numbers):

    # 버블 소트 정렬
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # 맥스값 초기화
    max_count = 0
    max_number = numbers[0]
    for number in numbers:
        # 카운트 초기화
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == number:
                count += 1
        # 버블소트로 인해 같을 경우 자동으로 더 큰 값이 적용
        if count>=max_count:
            max_count = count
            max_number = number

    return max_number, max_count





for tc in range(1, T+1):
    # 카드장수 N
    N = int(input())
    # 카드 숫자 리스트
    numbers = list(map(int,input()))
    result = max_card(N, numbers)
    
    print("#{} {} {}".format(tc,result[0],result[1] ))

