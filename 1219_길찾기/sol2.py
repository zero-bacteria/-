import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    # tc가 나와있으므로 그냥 받아오자
    # E도 받아오자
    tc, E = list(map(int, input().split()))
    # E만큼의 정보가 넘어올 것이다.
    # 각각의 시작 끝이 공백으로만 구분되어 반복하여 넘어올것이다.
    # 따라서 먼저 리스트로 받아주자
    info = list(map(int, input().split()))
    # 나중에 info 에서 불러온 값을 할당해줄 수 있는 데이터 저장공간을 만들자
    # 문제에서 주어진대로 풀은것
    # 2개의 길밖에 없기 때문에 두개의 리스트로 표현해주자
    route1 = [[]for _ in range(100)]
    route2 = [[]for _ in range(100)]
    for i in range(E):
        # 시작값은 0부터 짝수에
        # 끝값은 1부터 홀수에
        start_node = info[i*2]
        end_node = info[2*i+1]
        # 만약 route1에 정보가 없다면 1번에 저장해
        if not route1[start_node]:
            route1[start_node].append(end_node)
        # 이미 첫번째 길에대한 정보가 들어와있다면 route2에 저장해줘
        else:
            route2[start_node].append(end_node)

    # 0부터 시작합니다.
    stack = [0]
    # 방문검사합니다.
    visited = [False] * 100

    while stack:
        # 현재위치 불러와 봅시다.
        now = stack.pop()

        # 방문한적이 없으면?
        if not visited[now]:
            # 방문확인
            visited[now] = True
            # 루트1 부터 보자
            # 현재에 해당하는 길이 있다면 일단킵
            # 0번인덱스까지 써줘야 제대로 접근
            if route1[now]:
                stack.append(route1[now][0])
            # 루트 2보고 해당하는 길이 있다면 쌓아준다.
            if route2[now]:
                stack.append(route2[now][0])
            # 해당과정을 거치면 다음 회차에서 route2의 정보부터 탐색해서 간다음
            # route 2에 해당하는 가지? 들을 다거치고 route1로 돌아올 것이다.

    # 끝점에 방문한 흔적이 있어? 있으면 1 없으면 0
    result = 1 if visited[99] else 0


    print("#{} {}".format(tc, result))

