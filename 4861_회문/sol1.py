import sys
sys.stdin = open("input.txt")

T = int(input())

def my_reverse(line):
    r_line = []
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])
    return r_line

def palindrome(N,M,words):
    # 전체 크기가 N
    for i in range(N):
        # 가로검사
        for j in range(N-M+1):
            row = []
            col = []
            for k in range(M):
                row.append(words[i][j+k])
                col.append(words[j+k][i])
            if row == my_reverse(row):
                return row
            elif col == my_reverse(col):
                return col

for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]


    result = ''.join(palindrome(N, M, words))
    print("#{} {}".format(tc, result))

