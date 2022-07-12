'''
1. 아이디어
- BFS 사용(최단거리) => 상하좌우 1 존재
-
2. 시간복잡도
- O(V+E) = 500n
- V: n*m = 100n
- E: 4V = 400n
3. 자료구조
- 지도 int[][]
- 방문 bool[][]
'''

from collections import deque

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        ex, ey = q.popleft()

        for i in range(4):
            nx = ex + dx[i]
            ny = ey + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[ex][ey] + 1
    return graph[n - 1][m - 1]


print(bfs(0, 0))