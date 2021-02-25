my_list = [3, 9, 4, 7, 5, 0, 1, 6, 8, 2]

def quick_sort(numbers):
    N = len(numbers)
    if N <=1:
        return numbers
    else:
        # 기준점 설정
        pivot = numbers[0]
        # pivot을 기준으로 작은것 왼쪽 큰것 오른쪽넣을것
        # 그값 초기화
        left, right = [], []

        for idx in range(1, N):
            if numbers[idx] > pivot:
                right.append(numbers[idx])
            else:
                left.append(numbers[idx])
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        return [*sorted_left, pivot, *sorted_right]

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while  left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    # 실질적으로 pivot을 리턴
    return right

def quick_sort2(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        # 피봇을 기준으로 왼쪽 오른쪽 위해서 피봇 기준으로 실행
        quick_sort2(arr, start, pivot-1)
        quick_sort2(arr, pivot+1, end)
    return arr


print(my_list)
print(quick_sort(my_list))

print(my_list)
print(quick_sort2(my_list, 0, len(my_list)-1))

# pivot을 기준으로 왼쪽 오른쪽으로 나누는 것