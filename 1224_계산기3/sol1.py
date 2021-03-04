import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    # 계산식 길이 불러오기
    N = int(input())
    # 계산식을 직접 리스트에 넣어서 불러오기
    line = list(input())
    # isp, icp 설정
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, }
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, }
    # 스택 초기화
    stack = []
    # 계산할 항 초기화
    postfix = ''
    # line검사
    for char in line:
        # 만약 연산자 기호가 아니라면
        if not char in isp.keys():
            # 만약 닫힌 괄호가 왔다면
            if char == ')':
                # 열린괄호를 만날때까지 pop 해서 새로운 문장에 더해주기
                while True:
                    s = stack.pop()
                    if s == '(':
                        break
                    else:
                        postfix += s
            else:
                # 만약 숫자라면 postfix에 더해줌
                postfix += char
        else:
            # 만약 스택이 비어있다면 그냥 넣어주기
            if not stack:
                stack.append(char)
            else:
                # 만약 마지막스택보다 우선순위가 크다면 그냥 넣어주기
                # 들어가기 전이랑 들어가고나서랑 다른거 중요함
                # 들어가기전은 icp 들어가고나선 isp
                if icp.get(char) > isp.get(stack[-1]):
                    stack.append(char)
                else:
                    # 만약 우선순위가 낮다면 스택에서 빼서 식으로 옮겨주기
                    postfix += stack.pop()
                    # 그리고 새로운 연산자 넣어주기
                    stack.append(char)
    # 나머지 있는것들 다 빼주기
    for _ in range(len(stack)):
        postfix += stack.pop()

    # 스택 재활용해서 계산과정을 실행해보자
    for char in postfix:
        # 연산자 기호가 아니라면
        if not char in isp.keys():
            stack.append(char)
        # 연산자 기호라면
        else:
            # 먼저 뽑은게 다음거
            second = int(stack.pop())
            first = int(stack.pop())
            # 각각의 연산기호에 맞추어 계산한후 다시 넣어주기
            if char == '+':
                stack.append(first + second)
            elif char == '-':
                stack.append(first - second)
            elif char == '*':
                stack.append(first * second)
            elif char == '/':
                stack.append(first / second)

    result = stack.pop()

    print("#{} {}".format(tc, result))



