"""
1. 아이디어
- 5를 먼저 나눠 카운터에 몫을 더해준다
- 나머지를 3으로 나눠 카운터에 몫을 더해주고
- 나머지가 0이면 카운터를 출력 아니면 -1을 출력
2. 시간복잡도
- O()
3. 자료구조
- 배달해야할 사탕 : int
- 봉지수 : int

"""

import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

while(N >= 0):
    if N % 5 == 0:
        cnt += N//5
        print(cnt)
        break
    N -= 3
    cnt += 1

else:
    print(-1)