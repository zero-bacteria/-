import sys
sys.stdin = open("input.txt")

T = int(input())



for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = []
    for i in range(N):
        numbers.append(list(map(int, input().split())))

    max_value = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += numbers[i+k][j+l]

            if total >= max_value:
                max_value = total

    print("#{} {}".format(tc, max_value))