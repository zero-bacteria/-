import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    memory = list(input())
    now = ['0']*len(memory)
    count = 0
    for i in range(len(memory)):
        if memory[i] != now[i]:
            count += 1
            for j in range(i, len(now)):
                now[j] = memory[i]
    print("#{} {}".format(tc, count))

