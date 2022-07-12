'''
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(방문여부확인)
- 재귀함수에서 M개를 선택할 경우 print

2. 시간복잡도
- N! > 최대 10까지 현재 8까지 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 bool[]
'''

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
rs = []
chk = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)

            # 트리에서 다시 부모노드로 돌아가게 하는 기능
            chk[i] = False
            rs.pop()
recur(0)