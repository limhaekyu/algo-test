import sys
from collections import deque
input = sys.stdin.readline

q = deque([])
n = int(input())

while True:
    m = int(input().rstrip())
    if m == -1:
        break
    if m == 0:
        q.popleft()
    else:
        if len(q) < n:
            q.append(m)
        else:
            pass
if len(q) == 0:
    print('empty')
else:
    print(*q)



