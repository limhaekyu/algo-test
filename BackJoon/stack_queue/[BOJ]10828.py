import sys
input = sys.stdin.readline

n = int(input())
stack = []
comm = []
for i in range(n):
    comm.append(list(map(str, input().split())))

for i in comm:
    if i[0] == 'push':
        stack.append(i[1])
    elif i[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(len(stack)-1))
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
