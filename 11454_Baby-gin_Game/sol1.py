import sys
sys.stdin = open("input.txt")
# 두가지 방법이 있을것 함수 방법으로 푸는것과 일반로직
# 함수 이용해서 풀것
T = int(input())

def check_babygin(numbers):
    # counter = [0 for _in range(10)]
    counter = [0]*10

    #  babygin 체크
    is_babygin = 0

    # 카드 장수 세는 과정?
    for number in numbers:
        # 숫자에 해당하는 인덱스에 각각 더해줌
        counter[number] += 1

    # counter 만큼 돌면서 체크
    # for idx in range(len(counter)):

    #
    idx = 0
    while idx < len(counter):
        # triplet check
        if counter[idx]>=3:
            # 카드 세장 버리기
            counter[idx] -= 3
            # babygin 한걸음 다가가기
            is_babygin += 1

            # 숫자가 있는 한 계속 돌게 만들기 위해서 continue 삽입
            continue

        # run check
        # 8,9는 확인할 필요가 없음(뒤에 카드가 없기 때문에)
        if idx < 8:
            if counter [idx] and counter [idx+1] and counter[idx+2]:
                # 연속되는 카드 세장 하나씩 버리기
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                # 베이비진에 한걸음 다가가기
                is_babygin += 1
                # run 역시 두번 체크하기 위한 컨티뉴
                continue


        # 중간 계산 중에 베이비진이 등장 했다면
        if is_babygin == 2:
            return 1

        #  검증하고 나면 다음 idx로 넘어가기
        idx += 1

    #전부 돌때까지 베이비진이 등장하지 않았다면
    if is_babygin !=2:
        return 0







for tc in range(1, T+1):
    # 스플릿 안하는 이유?
    numbers = list(map(int, input()))
    # 0 과 1이 나오게 해야한다. (함수에서)
    result =  check_babygin(numbers)
    
    print("#{} {}".format(tc, result ))

