# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
# 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
# 문장 받아서 공백 기준으로 나눠서 리스트에 담아 lenth 반환

import sys
input = sys.stdin.readline

print(len(input().split()))