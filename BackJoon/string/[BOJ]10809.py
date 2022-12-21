# 일단 문자를 받고
# a->z 까지 갯수만큼 list 생성 -> 내부 value는 모두 -1
# for문 통해 index번호 list에 등록 (아스키코드 사용 -> a = 97 -> 아스키코드로 변환 후 -97 빼고 인덱스 등록
# 출력시 list 인덱스 순서대로 + 공백

text = input()

resultList = [-1] * 26

for i in range(len(text)):
    if resultList[ord(text[i]) - 97] != -1:
        continue
    else:
        resultList[ord(text[i]) - 97] = i

for i in range(26):
    print(resultList[i], end = ' ')
