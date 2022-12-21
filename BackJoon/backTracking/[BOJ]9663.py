"""
1. 아이디어
- 1차원 리스트를 통해 구현
- 리스트는 열이고 숫자를 통해 행을 입력
- 리스트에 있는 숫자가 반복되는 것 불가(한 줄에 같이 있는 경우), 대각선 좌,우 위의 행렬 검사
- 대각선 검사 방법 : for루프를 돌며 지금 arr[i] = n - 열 - i 와 n+열 을 통해 검사
- promising일 경우 cnt + 1

2. 시간복잡도
-
3. 자료구조
- 퀸이 놓여져 있는 좌표 : int[]
- 방법 수 : int

"""

import sys

input = sys.stdin.readline


# 한 줄에 있거나 대각선에 위치 할 경우 False를 반환
def is_promising(x):
    for k in range(x):
        if chess[k] == chess[x] or (x-k) == abs(chess[x]-chess[k]):
            return False
    return True


# 재귀를 이용해 x형 i열에 퀸을 놓고
# is_promising을 통해 퀸의 위치가 가능한지 확인
def dfs(x):
    global cnt
    if x == N:
        cnt += 1
    else:
        for i in range(N):
            chess[x] = i
            if is_promising(x):
                dfs(x+1)


N = int(input())
chess = [0] * N
cnt = 0
dfs(0)
print(cnt)
