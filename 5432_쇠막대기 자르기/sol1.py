import sys
sys.stdin = open("input.txt")

T = int(input())

def bar_cutting(info):

    # 쇠막대 초기값
    bar = 0
    # 레이저 맞는지 확인해 주는 것
    laser = 0
    # 결과값 초기화
    total = 0
    # 정보를 차례로 하나씩 살펴본다.
    for i in info:
        # 만약 괄호가 시작된 경우에는 두가지경우 막대시작 혹은 레이저 시작
        if i == '(':
            bar += 1
            laser = 1
        else:
            # 아니라면 막대기인지 레이저인지 판별
            # 레이저일경우에
            if laser:
                # 방금 열린괄호를 지나면서 온 것은 막대가 아니기 때문에 -1
                bar -= 1
                # 레이저가 끝났으니까 레이저는 0
                laser = 0
                # 레이저로 인해서 잘려진 왼쪽값을 더해준다
                total += bar
            else:
                # 한조각씩 늘어나게 된다.
                total += 1
                # 하나 닫힐때 마다 이미 카운팅 되었기 때문에 바 개수 감소
                # 때문에 새로 열려도 바의 개수는 유지할 수 있다.
                bar -= 1
    return total


for tc in range(1, T+1):
    info = input()
    result = bar_cutting(info)
    print("#{} {}".format(tc, result))

