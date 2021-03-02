import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    # 총시간은 두기차가 만나는 시간이 될것
    # 두기차가 만날때 까지 걸리는 시간
    t = D/(A+B)
    # 파리가 죽는 시간은 두기차가 만나느시간
    # 그동안 계속 같은속력으로 돌아다닐 것
    result = t*F
    
    print("#{} {}".format(tc, result))

