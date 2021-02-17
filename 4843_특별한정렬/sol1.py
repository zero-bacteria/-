import sys
sys.stdin = open("input.txt")

T = int(input())

def special_sort(N, numbers):
    new_list = []
    while numbers:
        max_value = 0
        max_idx = 0
        min_value = numbers[0]
        min_idx = 0
        for j in range(len(numbers)):
            if numbers[j] >= max_value:
                max_value = numbers[j]
                max_idx = j
            if numbers[j] <= min_value:
                min_value = numbers[j]
                min_idx = j
        new_list.append(max_value)
        new_list.append(min_value)
        if len(numbers) < 2:
            numbers.pop(max_idx)
        else:
            numbers.pop(max_idx)
            numbers.pop(min_idx)
    return new_list

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = ' '.join(map(str, (special_sort(N, numbers))))
    print("#{} {}".format(tc, result))

