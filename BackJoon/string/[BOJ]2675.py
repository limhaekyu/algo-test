# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 첫줄에 테스트케이스 갯수
# 숫자와 문자 받고 문자를 쪼개서 각각 숫자만큼 반복해서 출력

import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):

    num, s = input().split()
    resultText = ""

    for j in s:
        resultText += int(num) * j
    print(resultText)
