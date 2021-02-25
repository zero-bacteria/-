import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    # 돌아가야 할 방의 정보 받아오기
    move_info = [list(map(int, input().split())) for _ in range(N)]
    # 제일 많이 겹치는 것에 따라 시간 달라짐
    max_value = 0
    # 복도를 방문했는지 확인
    visited = [0]*201
    # 총학생수만큼
    for i in range(N):
        # 출발과 도착 지점
        # 두방이 마주보고 있으므로 복도 구역으로 생각한다면
        # 1과 2를 1번복도로 하기 위해서
        # +1을 해주고 2로 나눈 몫을 해줬음
        start = (move_info[i][0]+1)//2
        end = (move_info[i][1]+1)//2
        # 만약 첫번째로 받은 값이 더크면 그것은 도착값이므로
        # 두개 값을 바꿔준다
        if start > end:
            start, end = end, start
        # 복도에 돌아다닌 흔적 있으면 +1 해줌
        for j in range(start, end+1):
            visited[j] += 1
    # 최고로 많이 돌아다닌 복도 찾기
    for i in range(201):
        if visited[i] > max_value:
            max_value = visited[i]

    print("#{} {}".format(tc, max_value))

