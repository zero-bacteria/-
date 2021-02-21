import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 5줄의 워드들의 리스트
    words = [list(input())for _ in range(5)]
    # 결과값 초기값 설정
    result = []
    # 워드의 최대길이를 구하는 과정
    max_len = 0
    for i in range(5):
        if len(words[i]) > max_len:
            max_len = len(words[i])
    # 워드의 최대길이를 반복횟수
    for i in range(max_len):
        # 1줄씩 검사
        for j in range(5):
            # 만약 해당하는 줄이 최대길이보다 작거나 같다면 통과
            # '같은'이유는 위의 max_len의 범위가 idx 범위이기 때문에 1작다
            if len(words[j]) <= i:
                continue
            #  아니라면 더해주기
            result.append(words[j][i])
    result = ''.join(result)
    print("#{} {}".format(tc, result))

