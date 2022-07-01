'''
첫번째
1. 아이디어
    - for문으로 각 숫자의 위치에서 이후 K개의 수를 더함
    - 이때마다 최대값으로 갱신
2. 시간복잡도
    - for문 : O(N)
    - 각 위치에서 K개의 값을 더함 : O(K)
    - 총 O(NK) 1*10^5 * 10^5 >> 2억 --> X

3. 자료구조

두번째
1. 아이디어
    - 처음에 K개의 값을 구함
    - for문 : 다음 인덱스의 값을 더하고, 앞의 값을 뺌
    - 이때 최대값을 갱신
2. 시간복잡도
    - for문 : O(N) ==> 다음 인덱스 값 더하고, 앞의 값을 뺄 때 --> O(N)*2
3. 자료구조
    - 각 숫자들 N개 저장 배열 : int[]
        -> 숫자들 최대 100 > INT 가능
    - K개의 값을 저장 변수 : int
        -> 최대 : K * 100 = 1e5 * 100 = 1e7 > INT가능
    - 최대값 : int
'''

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
each = 0
# K개 더해주기
for i in range(K):
    each += nums[i]
maxv =  each

# 다음 인덱스 더해주고 이전 인덱스 빼주기
for i in range(K, N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)