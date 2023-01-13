import sys
input = sys.stdin.readline

n = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
count = end = 0

for s, e in time:
    if s >= end:
        count += 1
        end = e

print(count)