import sys
sys.stdin = open("input.txt")

T = 10

def check(numbers):
    # 숫자를 체크해서 지워주는 함수
    for i in range(len(numbers)-1):
        # 뒤의 숫자와 같다면
        if numbers[i] == numbers[i+1]:
            # 같은자리 2번 pop을 해줌 (하나씩 댕겨지기 때문)
            for _ in range(2):
                numbers.pop(i)
            # 지웠다면 함수 재호출
            return check(numbers)
    # 지운적이 없다면 출력
    return numbers

for tc in range(1, T+1):
    N, numbers = map(list, input().split())
    # 결과 불러오기
    result = check(numbers)
    print("#{} {}".format(tc, ''.join(result)))

