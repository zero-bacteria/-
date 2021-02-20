import sys
sys.stdin = open("input.txt")

T = 10

def my_reverse(line):
    r_line = []
    for i in range(len(line)-1, -1, -1):
        r_line.append(line[i])
    return r_line


for tc in range(1, T+1):
    N = int(input())
    words = [list(input())for _ in range(8)]

    count = 0
    for i in range(8):

        for j in range(8-N+1):
            row_temp = []
            col_temp = []
            for k in range(N):
                row_temp.append(words[i][j+k])
                col_temp.append(words[j+k][i])
            if row_temp == my_reverse(row_temp):
                count += 1
            if col_temp == my_reverse(col_temp):
                count += 1

    print("#{} {}".format(tc, count))

