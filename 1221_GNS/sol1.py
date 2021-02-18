import sys
sys.stdin = open("input.txt")

T = int(input())

def gsort(N, alien_numbers):
    # 통역을 해주는 딕셔너리
    translation= {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    # 숫자를 번역해서 리스트 대입
    numbers = []
    for i in range(len(alien_numbers)):
        numbers.append(translation.get(alien_numbers[i]))
    # 숫자 정렬
    numbers.sort()
    trans_reverse = {v:k for k,v in translation.items()}

    after = []
    for i in range(len(numbers)):
        after.append(trans_reverse.get(numbers[i]))

    return after

for tc in range(1, T+1):
    x , N = input().split()
    alien_numbers = list(input().split())
    result = ' '.join(gsort(N, alien_numbers))
    print("#{} {}".format(tc, result))

