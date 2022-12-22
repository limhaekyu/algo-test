# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램
# 첫째줄에 N개
# 한 줄씩 받아서 해당 index에 +1
# append는 메모리 재할당이 이루어져 메모리를 효율적으로 사용 못한다.

import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * 10001

for i in range(n):
    nums[int(input())] += 1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)