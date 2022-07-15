"""
1. 아이디어
- 2중 for문 -> 방문 x
- 1에 연결되어있는 노드 전부 바이러스
- 인접 값들 전부 queue에 담고, 바로 chk[]에 True로 바꿔준다.
2. 시간복잡도
- O(V+E)

3. 자료구조
- 그래프 : int[] (queue)
- 방문여부 : bool[]

"""

# 첫째줄 컴퓨터의 수
# 둘째줄 컴퓨터 쌍의 수

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
chk = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    chk[start] = True

    while queue:
        t = queue.popleft()

        for i in graph[t]:
            if not chk[i]:
                queue.append(i)
                chk[i] = True

bfs(1)

print(sum(chk) - 1)