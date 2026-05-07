def f(i):
    if len(t[i]) == 4:
        a.append('(')
        f(int(t[i][2]))
        a.append(t[i][1])
        f(int(t[i][3]))
        a.append(')')
    else:
        a.append(t[i][1])

for c in range(1, 11):
    a = []
    n = int(input())
    t = [[] for _ in range(n + 1)]
    for _ in range(n):
        d = input().split()
        t[int(d[0])] = d
    f(1)
    b = ''.join(a)
    print(f'#{c} {int(eval(b))}')