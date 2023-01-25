import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(graph[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max and not graph[nx]:
                graph[nx] = graph[x] + 1
                q.append(nx)

max = 100000
graph = [0]*(max+1)
n, k = map(int, input().split())

bfs()

