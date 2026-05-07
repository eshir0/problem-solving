T = int(input())
for _ in range(1,T+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    xy = []
    for i in range(N):
        xy.append((X[i],Y[i]))

    b = []
    for i in range(N):
        for j in range(i+1, N):
            c = E * ((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2)
            b.append((c,i,j))
    b.sort()

    p = [i for i in range(N)]

    def boss(x):

        while p[x] != x:
            x = p[x]
        return x

    ans = 0
    for c, i, j in b:
        bossi = boss(i)
        bossj = boss(j)

        if bossi != bossj:
            ans += c

            p[bossj] = bossi
    print(f'#{_} {round(ans)}')