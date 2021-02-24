import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0 for _ in range(V+1)]for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        node[i][j] = 1
    S, G = map(int, input().split())

    while cx == G:
        

    print("#{} {}".format(tc, result))

