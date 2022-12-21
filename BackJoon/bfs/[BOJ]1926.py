
'''
# 아이디어
- 2중 for문 => 값 == 1 && 방문 x
- bfs 돌면서 그림 +1, 방문 True
# 시간복잡도
- O(V+E)
- V = m*n = 500*500
- E = 4V = 4 * 500 * 500
- O = 5V = 5 * 500 * 500 = 1250000 < 2억 = OK!
# 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]

'''

from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range (m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)