# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,str(n)))
nums.sort(reverse= True)

for i in nums:
    print(i, end='')
