# N명이 응시, 가장 높은 점수 k명 상, 커트라인(상 받는 사람중 가장 낮은 점수의 사람) 구하기

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

list = list(map(int, input().split()))

list.sort()
print(list[len(list) - k])