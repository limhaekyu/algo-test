import sys
from collections import deque
input = sys.stdin.readline


# dfs
def dfs(v):
    check1[v] = 1
    print(v, end=' ')
    for i in range(n + 1):
        if check1[i] == 0 and tree[v][i] == 1:
            dfs(i)

# bfs
def bfs(v):
    q = deque()
    q.append(v)
    check2[v] = 1

    while(q):
        v = q.popleft()
        print(v, end=' ')
        for i in range(n+1):
            if check2[i] == 0 and tree[v][i] == 1:
                q.append(i)
                check2[i] = 1

n, m, v = map(int, input().split())
tree = [[0]*(n+1) for _ in range(n+1)]
check1 = [0]*(n+1)
check2 = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    tree[a][b] = tree[b][a] = 1

dfs(v)
print()
bfs(v)
