"""
- 문제 -
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
- 입력 -
첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.
- 출력 -
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

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