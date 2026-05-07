from collections import defaultdict
for _ in range(1,11):
    a,b = map(int,input().split())
    m = list(map(int,input().split()))
    c = []

    for i in range(0,len(m),2):
        c.append((m[i],m[i+1]))

    g = defaultdict(list)
    for u,v in c:
        g[u].append(v)
    print(g)
    q = [0]
    v = set([0])

    while q:
        c = q.pop()

        if c == 99:
            print(f'#{_} 1')
        for n in g[c]:
            if n not in v:
                v.add(n)
                q.append(n)
    print(f'#{_} 0')