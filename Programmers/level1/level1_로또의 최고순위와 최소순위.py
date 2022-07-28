"""
아이디어
- lottos의 숫자를 높은 수 부터 정렬
- lottos의 숫자가 0인지 확인
- zeroCnt +1
- lottos의 숫자가 win_nums에 있는지 확인
- 있다면 cnt +1
- 
"""

import sys
input = sys.stdin.readline

lottos = list(map(int,input()))
win_nums = list(map(int,input()))
lottos.sort(reverse = True)
win_nums.sort(reverse = True)

zeroCnt = 0
cnt = 0

def switch(key):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    return rank.get(key, 6)


def solution(lottos, win_nums):

    global zeroCnt
    global cnt

    for i in range(len(lottos)):
        if lottos[i] == 0:
            zeroCnt += 1
        else:
            if lottos[i] in win_nums:
                cnt += 1
    answer = []
    answer.append(switch(zeroCnt+cnt))
    answer.append(switch(cnt))

    return answer

print(solution(lottos, win_nums))