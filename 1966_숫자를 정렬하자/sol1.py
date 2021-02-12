import sys
sys.stdin = open("input.txt")

T = int(input())

def sort_n(N, numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    # 형태가 int 이므로 map으로 str 형태로 바꿔준 뒤 join
    result = " ".join(map(str,sort_n(N, numbers)))
    print("#{} {}".format(tc,result))

