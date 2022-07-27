import sys

input = sys.stdin.readline

absolutes = list(map(int, input()))
signs = list(map(int, input()))

result = 0


def solution(absolutes, signs):
    global result
    for i in range(len(absolutes)):
        if signs[i] == True:
            result += absolutes[i]
        else:
            result -= absolutes[i]
    return result


solution(absolutes, signs)
print(result)