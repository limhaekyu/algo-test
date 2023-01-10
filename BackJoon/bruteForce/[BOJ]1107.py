import sys
input = sys.stdin.readline

# 리모컨으로 동작 가능한 수인지 확인
def possible_num(x):
    x = list(str(x))
    for element in x:
        if element in broken:
            return False
    return True

n = int(input())
m = int(input())
broken = list(map(str, input().split()))

answer = abs(n - 100)

# abs 함수 사용으로 경우의 수가 50만에서 100만으로 늘어남
for i in range(1000001):
    if possible_num(i) is True:
        answer = min(answer, len(str(i)) + abs(n-i)) # 자릿수 + (원하는수 - 숫자)

print(answer)
