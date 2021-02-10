import sys
sys.stdin = open("input.txt")

T = int(input())

def ab_max(info, a_numbers, b_numbers):
    N=info[0]
    M=info[1]
    max_value = 0

    if M>N:
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += a_numbers[j]*b_numbers[i+j]
            if total >= max_value:
                max_value = total

    else:
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += a_numbers[i+j]*b_numbers[j]
            if total >= max_value:
                max_value = total


    return max_value





for tc in range(1, T+1):
    info = list(map(int,input().split()))
    a_numbers = list(map(int,input().split()))
    b_numbers = list(map(int,input().split()))
    result = ab_max(info, a_numbers, b_numbers)
    print("#{} {}".format(tc,result))

