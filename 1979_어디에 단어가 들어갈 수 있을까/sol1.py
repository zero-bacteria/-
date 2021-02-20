import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = []
    for i in range(N):
        numbers.append(list(map(int, input().split())))

    # # 범위 제한을 위해 오른쪽 끝 아래 끝에 0을 붙여서 제한을 둠
    # numbers.append([0 for _ in range(N)])
    # for number in numbers:
    #     number.append(0)


    x = 0
    y = 0
    count = 0
    total = 0
    for i in range(N):
        for j in range(N):
            if numbers[i][j]:

                total += 1
                if total > K:


            if not numbers[y][x]:







    print("#{} {}".format(tc, count))

