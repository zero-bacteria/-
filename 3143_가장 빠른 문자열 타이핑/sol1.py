import sys
sys.stdin = open("input.txt")

T = int(input())

def check(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[j+i] != B[j]:
                break
            if j == len(B)-1:
                for _ in range(len(B)):
                    A.pop(j-len(B)+1)
                return A
    return A

for tc in range(1, T+1):
    A, B = map(list,input().split())

    while X == A :
        X = check(A,B)


    print("#{} ".format(tc, ))

