import sys
sys.stdin = open("input.txt")

# 리스트? 방식으로 풀은 것
T = int(input())

for tc in range(1, T+1):
    # V와 E 받아옴
    V, E = map(int, input().split())
    # 리스트 방식? 으로 초기값 선언하자 노드값
    node = [[]for _ in range(V+1)]
    # E개만큼 연결되어 있기 때문에 범위 E로 설정
    for _ in range(E):
        # 각각의 연결관계를 받아오자
        start, end = map(int, input().split())
        # 연결관계를 표현하기 위해 추가해주자
        node[start].append(end)
    S, G = map(int, input().split())
    # 스택초기값
    stack = [S]
    # 방문검사
    visited = [False for _ in range(V+1)]
    # 스택이 존재하지 않을때 까지 반복
    while stack:
        # 현재 값을 스택에서 꺼내옴
        now = stack.pop()
        # 방문했다고 표시해줌
        visited[now] = True
        # 현재 노드의 정보 중에서
        # 각각의 리스트 들은 n번이 이어진 숫자들을 담고있다
        # 이중에서 반복문을 돌려서 검사를 한다.
        for next in node[now]:
            # 만약 다음 갈곳이 반복한적이 없던것이 있으면
            if not visited[next]:
                # 스택에 다음 갈곳의 정보를 넘겨준다.
                stack.append(next)
        # 이과정을 갈곳이 없을때 까지 반복

    # 출발점에서 시작해서 반복을했는데
    # 내가 말한곳에 다녀온적 있어? 도장찍어왔어?
    if visited[G]:
        # 왔으면 잘했어
        result = 1
    else:
        # 아니면 0...
        result = 0

    print("#{} {}".format(tc, result))

