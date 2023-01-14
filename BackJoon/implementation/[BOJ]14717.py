import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cases = 153
card = list(range(1, 11)) * 2

card.remove(a)
card.remove(b)

if a == b:
    result = (cases-(10-a))/cases
else:
    cnt = 0
    mine = (a+b)%10
    for i in range(18):
        for j in range(i+1, 18):
            if mine > (card[i]+card[j]) % 10 and card[i] != card[j]:
                cnt += 1
    result = cnt/cases

print(f'{result:.3f}')
