import sys
sys.stdin = open("input.txt")

T = int(input())

def str_count(str1, str2):
    str_list = list(set(str1))
    count_dict = {}
    for ch in str_list:
        count_dict[ch] = 0
        for s in str2:
            if ch == s:
                count_dict[ch] += 1

    max_value = 0
    for ch in str_list:
        if count_dict.get(ch) > max_value:
            max_value = count_dict.get(ch)

    return max_value



for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = str_count(str1, str2)
    print("#{} {}".format(tc, result))

