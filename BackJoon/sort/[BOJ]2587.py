# 줄마다 자연수 하나씩 다섯줄 평균과 중앙값을 구해라

import sys
input = sys.stdin.readline

nums = []
sum = 0

for i in range(0, 5):
    nums.append(int(input()))

nums.sort()

for i in nums:
    sum += i

print(int(sum/5))
print(nums[2])