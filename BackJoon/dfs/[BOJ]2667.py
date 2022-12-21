'''
1. 아이디어
- 인접한 V 먼저 검색
- 재귀로 반복 (더이상 없을 떄까지)
- 다시 돌아와서 반복
- 2중 for문 -> 1 && 방문 X => dfs


2. 시간복잡도
- O(V+E) = 5N^2 = N^2 = 625
- V = N^2
- E = 4*N^2

3. 자료구조
- map : int[][]
- chk : bool[][]
- res : int[][]
'''


import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)] # \n 값 날려주는 함수 strip()
chk = [[False]*N for _ in range(N)]

result = []
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0<=nx<N and 0<=ny<N:
            if graph[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if graph[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))

for i in result:
    print(i)
