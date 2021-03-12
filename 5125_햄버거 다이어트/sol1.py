import sys
sys.stdin = open("input.txt")

T = int(input())

def hamburger(idx, now_cal, now_fla):
    # 최고값 사용
    global max_value
    # 함수 종료조건을 주어야 한다.
    # 먼저 칼로리를 넘지 않아야 하기 때문에
    # 칼로리 넘으면 끝임
    if now_cal > L:
        return
    # 더 맛있어졌으면 갱신
    if max_value < now_fla:
        max_value = now_fla
    # 마지막까지 검사를 마쳤다면 끝
    if idx == N:
        return
    # 맛과 칼로리 정보 받아오기
    fla = info[idx][0]
    cal = info[idx][1]
    # 재료를 아무것도 안넣었는 경우에는 그대로 호출
    hamburger(idx+1, now_cal, now_fla)
    # 재료를 넣는경우는 새로 더해서 갱신해서 호출
    hamburger(idx + 1, now_cal + cal, now_fla + fla)

for tc in range(1, T+1):
    N, L = map(int, input().split())
    info = []
    for i in range(N):
        info.append(list(map(int, input().split())))
    max_value = 0
    # 맨처음 값들은 모두 0
    hamburger(0, 0, 0)
    print("#{} {}".format(tc, max_value))



