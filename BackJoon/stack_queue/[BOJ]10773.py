import sys
input = sys.stdin.readline

k = int(input())
nums = []
num_list = []

for i in range(k):
    nums.append(int(input()))

for i in nums:
    if i == 0:
        num_list.pop(len(num_list)-1)
    else:
        num_list.append(i)

print(sum(num_list))