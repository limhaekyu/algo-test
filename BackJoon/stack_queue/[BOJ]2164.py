# 정수 n
# 1~n 까지 수
# 젤 밑 (1)이 빠지고나서 젤밑에 있던 숫자가 젤위로 올라옴 반복
# 마지막 남은 카드 구하기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(1,n+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])