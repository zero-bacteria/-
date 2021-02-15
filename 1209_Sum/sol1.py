import sys
sys.stdin = open("input.txt")

T = 10

def search_sum(numbers):
    max_value = 0

    for i in range(len(numbers)):
        total = 0

        for j in range(len(numbers[i])):
            total += numbers[i][j]
        if total >= max_value:
            max_value = total

    for i in range(len(numbers)):
        total = 0

        for j in range(len(numbers[i])):
            total += numbers[j][i]
        if total >= max_value:
            max_value = total
    total = 0
    for i in range(len(numbers)):
        total += numbers[i][i]
        if total >= max_value:
            max_value = total
    total = 0
    for i in range(len(numbers)):
        total += numbers[i][99-i]
        if total >= max_value:
            max_value = total

    return max_value

for tc in range(1, T+1):
    tt = int(input())
    numbers = []
    for i in range(100):
        numbers.append(list(map(int,input().split())))
    result = search_sum(numbers)
    print("#{} {}".format(tc,result ))

