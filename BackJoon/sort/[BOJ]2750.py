# N개의 수 주어졌을 때, 오름차순으로 정렬
# 첫째줄 줄의 갯수
# 리스트에 순서대로 담아서 정렬

n = int(input())
m_list = []
for i in range(n):
    m_list.append(int(input()))

m_list.sort()

for i in m_list:
    print(i)

