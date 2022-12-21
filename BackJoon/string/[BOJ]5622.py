# 주어진 단어를 통해 전화 다이얼을 돌려야한다
# 1~0 까지 1을 누르려면 1초 1씩 늘어날 때 마다 1초씩 늘어난다.

import sys

input = sys.stdin.readline

s = input()
time = 0

def dial(a):
    if a == 'A' or a == "B" or a == "C":
        return 2
    elif a == 'D' or a == 'E' or a == 'F':
        return 3
    elif a == 'G' or a == 'H' or a == 'I':
        return 4
    elif a == 'J' or a == 'K' or a == 'L':
        return 5
    elif a == 'M' or a == 'N' or a == 'O':
        return 6
    elif a == 'P' or a == 'Q' or a == 'R' or a == 'S':
        return 7
    elif a == 'T' or a == 'U' or a == 'V':
        return 8
    elif a == 'W' or a == 'X' or a == 'Y' or a == 'Z':
        return 9

for i in range(len(s)-1):
    time += int(dial(s[i]))+1

print(time)


