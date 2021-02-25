import sys
sys.stdin = open("input.txt")

# 인접행렬 방식으로 풀은 것
T = int(input())

# 시작점 부터 끝점까지 도달할 수 있는지에 대한 함수
def dfs(start, end):
    # 스택 초기화
    stack = []
    # 방문 여부를 검사할 행렬
    # 인덱스 값이므로 +1을 해주어 혼동 x
    visited = [False] * (V + 1)
    # 시작점을 스택에 삽입해준다
    stack.append(start)

    # 스택이 빌때까지 반복문 돌려준다.
    while stack:
        # 지금 현재 스택을 꺼내어 현재 값에 할당
        now = stack.pop()
        # 현재 들렀다는 것을 표시
        visited[now] = True
        # 1부터 V+1범위 까지 살펴봄
        for next in range(1, V+1):
            # 만약 방문하지 않았고
            # 또한 연결되어 있다면 (값이 1이라면)
            if not visited[next] and node[now][next]:
                # 갈수있는 곳 이므로 스택에 더해준다.
                stack.append(next)
    # 만약 끝점에 들른흔적이 있다면?
    if visited[end]:
        # 들렀다는 것을 표시
        return 1
    else:
        # 아니라면 안들렸다는 것을 표시
        return 0

for tc in range(1, T+1):
    # V와 E 받아오기
    V, E = map(int, input().split())
    # 노드를 인접행렬로 나타내기 위한 0으로 이루어진 초기값
    # 인덱스 값이므로 V+1을 해주어 혼동되지 않도록 하자
    node = [[0 for _ in range(V+1)]for _ in range(V+1)]
    # 연결선 E 만큼 반복해주면서 연결되어있는가를 파악
    for _ in range(E):
        # 시작점과 끝점을 각각 받아옴
        start, end = map(int, input().split())
        # 해당하는 인접행렬에 할당해줌
        # 방향성이 있음
        node[start][end] = 1
    # 검사를 위한 시작점과 끝점의 값을 가져옴
    S, G = map(int, input().split())
    # 원하는 구간이 연결되어 있는가 검사한 값을 출력
    print("#{} {}".format(tc, dfs(S, G)))

