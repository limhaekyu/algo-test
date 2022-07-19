"""
1. 아이디어
- dfs를 통해 간선을 연결하고
- cont를 통해 연결 요소의 갯수를 구한다
- 방문하지 않은 노드는 방문처리를 해주는 방식으로 구현

2. 시간복잡도
- O(V+E) : N + N^2-N = O(N^2)
- V : N
- E : N(N-1)/2
3. 자료구조
- 그래프 : int[]
- 카운트 : int
- 방문여부 : bool[]
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
chk = [False] * (N+1)

cnt = 0

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(v):
    chk[v] = True
    for i in graph[v]:
        if chk[i] == False:
            chk[i] = True
            dfs(i)

for i in range(1, N+1):
    if chk[i] == False:
        cnt += 1
        dfs(i)

print(cnt)