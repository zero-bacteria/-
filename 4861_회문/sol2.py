import sys
sys.stdin = open("input.txt")

T = int(input())

def palindrome(N, M, chars):





for tc in range(1, T+1):
    N, M = map(int, input().split())
    chars = []
    for i in range(N):
        temp = []
        temp_char = input()
        for t in temp_char:
            temp.append(t)
        chars.append(temp)
    result = palindrome(N, M, chars)
    print("#{} {}".format(tc, result))

