import sys
sys.stdin = open("input.txt")

T = 10

def view(N,numbers):
    # 카운트 값 초기화
    count = 0
    # N만큼의 길이에 대해서
    for i in range(N):
        # 층수가 0일 경우는 세대가 없으므로 생략
        if numbers[i] != 0:
            # 각 아파트 마다 층수 반복문
            for j in range(1,numbers[i]+1):
                # 초망권 체크 변수
                check = 0
                # 좌우 2세대 점검
                for k in range(i-2,i):
                    # 만약 j층이 왼쪽 k층에 가려진다면
                    if j <= numbers[k]:
                        check+=1
                for k in range(i+1, i+3):
                    # 오른쪽 검사
                    if j <= numbers[k]:
                        check+=1
                #아니라면 카운트 +1
                if check == 0:
                    count+=1

    return count






for tc in range(1, T+1):
    N= int(input())
    numbers = list(map(int,input().split()))
    result = view(N,numbers)
    print("#{} {}".format(tc,result))

