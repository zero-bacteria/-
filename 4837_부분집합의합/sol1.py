import sys
sys.stdin = open("input.txt")

T = int(input())

def subset(info):
    # N과 K 값을 임의로 설정한 리스트에서 하나씩 받아옴
    N = info[0]
    K = info[1]
    # 1부터 12까지의 범위의 리스트 설정
    A = [i for i in range(1,13)]

    # 전체 초기값 설정
    numbers = []
    # 부분집합 구하는과정
    for i in range(1<<12):
        sub_numbers = []
        for j in range(12):
            if i&(1<<j):
                # 부분집합 리스트를 생성
                sub_numbers.append(A[j])
        # 만약 부분집합 리스트의 길이가 원하는 N 이라면 전체 리스트에 삽입
        if len(sub_numbers) == N:
            numbers.append(sub_numbers)
    # 카운트 초기화
    count = 0
    # 내장함수 sum 대신 total로 합을 구해서 원하는 값이 나오면 카운트
    # 내장함수 사용시 위의 반복문에서 종료 가능
    for i in range(len(numbers)):
        total = 0
        for j in numbers[i]:
            total += j
        if total == K:
            count += 1

    return count


for tc in range(1, T+1):
    info = list(map(int, input().split()))
    result = subset(info)
    print("#{} {}".format(tc, result))

