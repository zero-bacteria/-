import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    line = list(map(str, input()))
    stack = []
    # line을 검사
    for i in range(len(line)):
        # 만약 스택에 값이 없다면 스택에 추가
        if not stack:
            stack.append(line[i])
        #이미 들어간 값이 있을때
        else:
            #  마지막으로 추가된 값이 현재 검사하는 값과 같다면
            if stack[-1] == line[i]:
                # 마지막 값을 pop해서 없애줌
                stack.pop()
            else:
                # 그렇지 않다면 그냥 더해줌
                stack.append(line[i])
    # 결과는 스택 즉 중복되지 않은 값들을 받아온 것의 길이
    result = len(stack)
    print("#{} {}".format(tc, result))

