# 대소문자로 된 단어가 주어지면 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램 (대,소문자 구분 x)
# 여러개 존재하는 경우 ?출력

# 입력받고 모두 소문자로 변경
# list map 사용해 key = 알파벳, value = 갯수

import sys
input = sys.stdin.readline

d = {}
text = str(input()).upper()

for i in text:
    if i != '\n':
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
max_keys = [key for key, value in d.items() if value == max(d.values())]

if len(max_keys) >= 2:
    print("?")
else:
    print(max_keys[0])

# '\n'이 입력된다.