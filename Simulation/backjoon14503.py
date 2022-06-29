'''
1. 아이디어
    - 특정조건 만족하는 한 계속 이동 while -> 조건 x break;
    - 4방향 탐색 먼저 수행 -> 빈칸 있을 경우 이동
    - 4방향 탐색이 안될 경우, 뒤로 한칸 가서 반복 -> 뒤 x 종료
2. 시간복잡도
    - while문 최대 : N x M < 2억
    - O(NM) : N x M x 4
    - 각 칸에서 4방향 연산 수행
3. 자료구조
    - 전체지도 : int[][]   -> 0: 청소 x, 1: 벽, 2: 청소 O
    - 내위치, 방향 : int(x), int(y), int(d)
    - 전체, int(cnt)
'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
y,x,d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1
    sw = False
    for i in range(1,5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 0:
                d = (d-i+4)%4         # 방향 회전
                y = ny
                x = nx
                sw = True
                break           # while 문으로 이동

    # 4방향 모두 있지 않을 때
    if sw == False:
        ny = y - dy[d]
        nx = x - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)