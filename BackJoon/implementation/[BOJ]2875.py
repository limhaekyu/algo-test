import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

team = 0

while n >=2 and m >=1 and n+m-3>=k :
    n -=2
    m -=1
    team +=1
print(team)