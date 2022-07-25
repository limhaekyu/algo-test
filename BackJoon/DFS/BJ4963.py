"""

1. 아이디어
- 0 0 을 입력 받을 때 까지 계속 입력을 받는다
- dfs를 사용해 인접한 좌표들을 방문 처리한뒤 섬의 갯수를 올려준다.
-
2. 시간복잡도
- O(V+E)
- V : 50
- E : 50
3. 자료구조
- 지도 : int[]
- 섬의 수 : int
"""

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = [-1, 0, 1, 0, -1, 1, 1, -1]
dy = [0, -1, 0, 1, 1, 1, -1, -1]

def dfs(x, y):
    island[x][y] = -1  # 방문체크

    for i in range(8): # 인접좌표 돌기
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break                           # 입력이 0 0 이면 break

    island = [list(map(int, input().split())) for _ in range(h)] # 한줄 한줄 입력
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)