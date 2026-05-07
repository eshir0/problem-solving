for c in range(1,11):
    l, s = map(int, input().split())
    d = list(map(int,input().split()))

    g = [[] for _ in range(101)]
    for i in range(0,l,2):
        g[d[i]].append(d[i+1])

        v = [0] * 101
        v[s] = 1
        q = [s]

        for n in q:
            for x in g[n]:
                if not v[x]:
                    v[x] = v[n] + 1
                    q.append(x)
        ans = max(i for i, depth in enumerate(v) if depth == max(v))
    print(f'#{c} {ans}')