import sys
sys.stdin = open("input.txt")

T = int(input())

def bubble_sort(numbers):
    for i in range(len(numbers)-1,0,-1):
        for j in range(0,i):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = bubble_sort(numbers)
    result = []
    for i in range(5):
        result.append(numbers[len(numbers)-1-i])
        result.append(numbers[i])
    result = ' '.join(map(str, result))
    print("#{} {}".format(tc, result))

