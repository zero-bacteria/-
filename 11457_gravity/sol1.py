import sys
sys.stdin = open("input.txt")
# 내가 한것
T = int(input())


def gravity_check(numbers):
    #최고값
    max_value=0
    for i in range(len(numbers)):
        # 낙차를 하나씩 더해줌
        l = 0
        # 같은 라인의 블록을 만나면 카운트 x
        for j in range(i+1,len(numbers)):
            if numbers[i] > numbers[j]:
                l += 1

        if l>=max_value:
            max_value = l
    return max_value

# 이전 코드에서 틀렸던 이유
# 1. 같지 않을때 조건을 두어서 -> 클때로 조건을 두어야 한다.
# 2. N을 반복하는 구조를 두지 않아 다음 케이스때부터는 무조건 틀릴 수 밖에 없었다.

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    result = gravity_check(numbers)
    print("#{} {}".format(tc,result))



