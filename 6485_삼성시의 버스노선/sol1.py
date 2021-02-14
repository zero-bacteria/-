import sys
sys.stdin = open("input.txt")

T = int(input())

def bus_route(N,numbers,P,C):
    # 정류장 들르는 것을 확인하기 위해 초기값 설정
    result = [0]*P
    # N만큼 반복하며 노선 조건 불러오기
    for i in range(N):
        # P만큼 반복하며 정류장 C가 조건에 해당하는지 검사
        for j in range(P):
            if numbers[i][0] <= C[j] <= numbers[i][1]:
                # 검사 결과 반영
                result[j] += 1
    return result


for tc in range(1, T+1):
    # N 받아옴
    N = int(input())
    # N에 따른 리스트의 길이가 달라질 수 있으므로 초기값생성
    numbers = []
    # N 만큼 반복을 통해 리스트 안의 리스트 생성
    for i in range(N):
        numbers.append(list(map(int, input().split())))
    # P를 받아옴
    P = int(input())
    # numbers와 마찬가지로 C도 동일한 구조로 실행
    C = []
    for j in range(P):
        C.append(int(input()))
    result = " ".join(map(str, bus_route(N, numbers, P, C)))
    print("#{} {}".format(tc,result))





