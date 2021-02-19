import sys
sys.stdin = open("input.txt")

T = int(input())

def palindrome(N,M,chars):

    col_chars = []
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += chars[j][i]
        col_chars.append(temp)

    for ch in chars:
        for i in range(N-M+1):
            words = ''
            for j in range(i, M+i):
                words += ch[j]
            for k in range(M // 2):
                if words[k] != words[-1 - k]:
                    continue
                    return words

    for ch in col_chars:
        for i in range(N - M + 1):
            words = ''
            for j in range(i, M + i):
                words += ch[j]
            for k in range(M // 2):
                if words[k] != words[-1 - k]:
                    continue
                    return words

for tc in range(1, T+1):
    N, M = map(int, input().split())
    chars = []
    for i in range(N):
        chars.append(input())
    result = palindrome(N, M, chars)
    print("#{} {}".format(tc, result))

