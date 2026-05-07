N = int(input())
stack = []
r = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            r.append(-1)
        else:
            r.append(stack.pop())
    elif cmd[0] == 'size':
        r.append(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            r.append(1)
        else:
            r.append(0)
    elif cmd[0] == 'top':
        if len(stack) == 0:
            r.append(-1)
        else:
            r.append(stack[-1])
print()
for i in range(len(r)):
    print(r[i])