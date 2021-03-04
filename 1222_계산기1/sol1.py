import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    # 계산식 길이 불러오기
    N = int(input())
    # 계산식을 직접 리스트에 넣어서 불러오기
    line = list(input())
    # 스택 생성
    stack = []
    # 계산을 실행해줄 것 만들음
    postfix = ''
    # 리스트를 돌면서 검사하면서 피연산자만 남기는 과정
    for i in range(N):
        # 만약 i번째에 +가 온다면
        if line[i] == '+':
            # 스택이 비어있다면 그냥 추가
            if not stack:
                stack.append(line[i])
            # 만약 스택에 +가 있다면
            # 우선순위가 같으므로
            # 기존의 것을 뽑고 새로 넣어주는게 원칙
            else:
                postfix += stack.pop()
                stack.append(line[i])
        else:
            # 숫자를 더해주기
            postfix += line[i]
    # 맨마지막에 스택에 남아있을 것이므로 마지막에 붙여주자
    postfix += stack.pop()

    # 이제 만들어 준 것을 연산하는 과정
    # 스택을 재활용해서 사용한다.
    for i in postfix:
        # 숫자가 오게된다면
        if not i == '+':
            # 스택에 숫자로 변환해서 더해줌
            stack.append(int(i))
        else:
            # 플러스가 오게된다면 합을 실행하라는 소리이므로
            # 숫자 두개를 뽑아 더해준뒤
            # 다시 넣어준다.
            stack.append(stack.pop() + stack.pop())
    # 스택에 결과값만이 남아 있을것이다.
    result = stack.pop()

    print("#{} {}".format(tc, result))

