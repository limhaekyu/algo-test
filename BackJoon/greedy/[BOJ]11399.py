"""

1. 아이디어
- 먼저 걸리는 시간을 리스트로 담고 정렬한다.

- 전체 걸리는 시간의 값에다가 계속 더해준다.
2. 시간복잡도
- O(N)

3. 자료구조
- 각자 걸리는시간 : int[]
- 총 걸리는시간 : int

"""

import sys
input = sys.stdin.readline

N = int(input())
P = [int(i) for i in input().split()]
P.sort()
total = 0

for i in range(N):
    total += P[i]
    if i<N-1:
        P[i+1] +=  P[i]

print(total)