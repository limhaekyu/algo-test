
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
#
# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

# 입력 n

# n의 분해합은 n과 n을 이루는 각 자리수 합 234 -> 234+2+3+4
# 분해합 : m
# m, n 생성자


import sys

input = sys.stdin.readline

n = int(input())
result = 0

for i in range(1, n+1):
    n_list = list(map(int, str(i)))
    s = i + sum(n_list)
    if s == n:
        result = i
        break

print(result)

