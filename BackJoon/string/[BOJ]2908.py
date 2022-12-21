# 수를 거꾸로 읽으며 두 수를 비교한다.
# 두 수가 붙어서 000 000 형식으로 입력, 세 자리 수
# 각각 split으로 받아서 뒤집어서 비교

import sys
input = sys.stdin.readline

n,m = input().split()
n_reverse = int(str(n)[::-1])
m_reverse = int(str(m)[::-1])

if n_reverse > m_reverse:
    print(n_reverse)
else:
    print(m_reverse)