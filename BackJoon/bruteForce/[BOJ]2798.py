# 딜러 N장 숫자 보이도록 바닥, 숫자 M 외침
# 플레이어 N장 중 3장 pick, 합이 M을 넘지 않고 최대한 크게
# 입력 : N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000),
# 입력 : 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
# 조건 : M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i]+nums[j]+nums[k] > m:
                continue
            else:
                result = max(result, nums[i]+nums[j]+nums[k])
print(result)
