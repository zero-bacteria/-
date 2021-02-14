import sys
sys.stdin = open("input.txt")

T = int(input())

def factorization(N):
    # 각각의 소인수 분해할 소수 리스트
    target = [2,3,5,7,11]
    # 결과 초기값
    result = []

    # 원하는 리스트 내에서 반복
    for n in target:
        # 카운트 초기화
        count = 0
        #  N을 n(원하는 소수) 로 나누어 지면 반복
        while not N%n :
            # N을 n으로 나눠줌
            N = N/n
            # 횟수 더해줌
            count += 1
        # 해당 소수가 몇번 나누어졌는지 기록
        result.append(count)
    return result

for tc in range(1, T+1):
    N = int(input())
    result = " ".join(map(str, factorization(N)))
    print("#{} {}".format(tc, result))

