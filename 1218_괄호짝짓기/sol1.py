import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    # 문자 길이
    N = int(input())
    # 문자열 받아옴
    line = input()
    # 스택 설정
    stack = []
    # 괄호를 딕셔너리로 만듬
    dict = {')': '(', '}': '{', '>': '<', ']': '['}
    # 결과값 초기화
    result = 1
    # 문자를 돌면서 검사
    for char in line:
        # 미리 설정해놓은 dict 값에 있다면 즉, 열린괄호라면
        if char in dict.values():
            # 스택에 더해줌
            stack.append(char)
        else:
            # 열린괄호 외에는 닫힌괄호이므로
            # 닫힌괄호가 왔을때 해당하는 dict의 value 값이 스택의 마지막값과 다르다면
            # 즉 괄호가 순서가 맞지 않다면
            if dict.get(char) != stack.pop():
                result = 0
                break
    print("#{} {}".format(tc,result))

