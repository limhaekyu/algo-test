from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
counts = Counter(nums).most_common()

print(round(sum(nums) / len(nums)))
print(nums[n // 2])
if len(counts) > 1:
    if counts[0][1] == counts[1][1]:
        print(counts[1][0])
    else:
        print(counts[0][0])
else:
    print(counts[0][0])

print(nums[-1] - nums[0])