import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
count = []

for _ in range(N):
    board.append(input())

# 전체 체스판을 검사하기위해 시작점을 잡기위해 -7을 한다.
# index1, index2는 시작점이 black인지 white인지 확인하기 위한 것
for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))