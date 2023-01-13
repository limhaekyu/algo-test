# 아이디어
# 1. 첫 주유소에서 기름을 다음 도시까지 가는 거리만큼 넣고
# 2. 다음 주유소와 비교해서 작음 주유소에서 다음까지가는 거리만큼 추가 하는 방식으로 진행

import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost = 0
total = 0

for i in range(n-1):
    if i != 0:
        if min_cost < cost[i]:
            total += km[i]*min_cost
        else:
            total += km[i]*cost[i]
            min_cost = cost[i]

    else:
        total += cost[i] * km[i]
        min_cost = cost[i]

print(total)