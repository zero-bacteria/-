import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    # tc가 나와있으므로 그냥 받아오자
    # E도 받아오자
    tc, E = list(map(int, input().split()))
    # 정보 매트릭스를 만들어보자
    # 100까지하면 99 까지 만들어 진다 계속 하지만 인덱스값과 혼동하지 않기 위해 0은 x
    edge_matrix = [[0 for _ in range(100)]for _ in range(100)]
    # 각각의 정보들을 불러온다.
    edge_input = list(map(int, input().split()))

    # E 만큼의 길이 있을것이다
    for i in range(E):
        # 0부터 시작해서 시작 노드는 2의 배수에 있을 것이고
        start_node = edge_input[i*2]
        # 도착 노드는 홀수에 있을 것이다.
        end_node = edge_input[i*2+1]
        #  각각의 값을 받아와서 2차원 배열에 저장해주자
        edge_matrix[start_node][end_node] = 1
    # 방문증 검사
    visited = [False] * 100
    # 문제에서 주어진 것 처럼 무조건 0부터 시작 따라서 stack 초기값에 0넣어주자
    stack = [0]

    # 스택이 있을 때 까지 반복
    while stack:
        # 현재 값을 받아오자
        now = stack.pop()
        # 만약 방문한 적이 없다면
        if not visited[now]:
            # 방문했다고 도장찍어줘
            visited[now] = True
            #  모든 노드 반복하면서 다음 갈곳을 찾아보자
            for next in range(100):
                # 만약 방문하지 않았고 연결이 되어 있다면
                if not visited[next] and edge_matrix[now][next] == 1:
                    # 스택에 넘겨줘
                    stack.append(next)
    # 끝점에 방문한 흔적이 있어? 있으면 1 없으면 0
    result = 1 if visited[99] else 0

    print("#{} {}".format(tc, result))

