import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 단어 받아오기
    words = list(input())
    # temp 초기화
    temp = []
    # 레인지 오류를 막기위해 -1 한건데 상관없을듯 어차피 그전에 끝남
    for i in range(len(words)-1):
        # temp에 하나씩 추가해줌
        temp.append(words[i])
        # temp의 첫단어가 다음에 다시나온다?
        if temp[0] == words[i+1]:
            # 그다음부터 템프의 길이만큼 비교해봤을때 같으면 끝
            if temp == words[i+1:i+len(temp)+1]:
                break
    result = len(temp)
    print("#{} {}".format(tc, result))

