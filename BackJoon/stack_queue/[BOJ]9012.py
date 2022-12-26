import sys
input = sys.stdin.readline

t = int(input())
brackets = []
for i in range(t):
    brackets.append(input())

for i in brackets:
    count = 0
    bracket = list(i.strip())
    chk = 0

    for j in bracket:
        if j == '(':
            count += 1
        elif j == ')':
            if count == 0:
                chk = 1
            else:
                count -= 1

    if chk == 0 and count == 0:
        print('YES')
    else:
        print('NO')
