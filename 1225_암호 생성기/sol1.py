import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    # tc 귀찮지만 준거 쓰자
    tc = int(input())
    numbers = list(map(int, input().split()))
    # 맨처음 포문으로 했다가 실패해서 그냥 i 지정
    # i의 초기값은 1
    i = 1
    # 계속 돈다
    while True:
        # 맨앞을 팝 해주어서 i만큼 뺀 값을 임시 저장
        temp = numbers.pop(0) - i
        # 저장된 값이 0보다 작으면 그냥 0해
        if temp < 0:
            temp = 0
        # 그 값을 맨뒤로 다시 더해줌
        numbers.append(temp)
        # 만약 저장된 값이 0이 나오게 된다면 끝
        if temp == 0:
            break
        # 안끝났으면 1더해줌
        i += 1
        # 5보다 커지면 다시 1부터 시작
        if i > 5:
            i = 1
    result = ' '.join(list(map(str, numbers)))
    print("#{} {}".format(tc, result))