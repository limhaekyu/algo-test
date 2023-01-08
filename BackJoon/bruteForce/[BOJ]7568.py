# n 입력
# 줄마다 체중, 신장
# 체중과 신장 둘다 커야지 덩치가 큰 것

# 한 줄씩 [kg,cm]로 리스트에 담는다.
# 리스트를 하나하나 비교하면서 cnt

import sys

input = sys.stdin.readline

n = int(input())
n_list = []
rank_list = []

for i in range(n):
    n_list.append(list(map(int, input().split())))

for i in n_list:
    rank = 1
    for j in n_list:
        if (i[0] < j[0]) and (i[1] < j[1]):
            rank += 1
    rank_list.append(rank)
    print(rank, end=" ")

