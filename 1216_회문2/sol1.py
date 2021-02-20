import sys
sys.stdin = open("input.txt")

T = 10

def palindrome(words, n):
    for i in words:
        for j in range(100-n+1):
            for k in range(n//2):
                if i[j+k] != i[j+n-1-k]:
                    break
                else:
                    return n
    return 0

for tc in range(1, T+1):
    t = int(input())
    words = [list(input())for _ in range(100)]
    t_words = list(zip(*words))

    for n in range(100,-1,-1):
        if palindrome(words, n) == n or palindrome(t_words, n) == n:
            result = n
            break

    print("#{} {}".format(tc, result))

