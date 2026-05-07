for T in range(1,int(input())+1):
    N, M, C = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(N)]

    a = []

    def ck(a,C):
        mp = 0

        def dfs(idx,cs,cp):
            nonlocal mp
            
            if cs > C:
                return

            if idx == len(a):
                if cp > mp:
                    mp = cp
                return

            dfs(idx + 1, cs + a[idx], cp +  (a[idx] ** 2))

            dfs(idx + 1, cs, cp)
        dfs(0,0,0)
        return mp        

    for i in range(N):
        for j in range(N-M+1):
            a.append((ck(m[i][j:j+M],C),i,j))

    b = 0

    for i in range(len(a)):
        for j in range(len(a)):
            z1,y1,x1 = a[i]
            z2,y2,x2 = a[j]
            if y1 != y2:
                b = max(b,z1+z2)
            elif abs(x1 - x2) >= M:
                b = max(b,z1+z2)       

    print(f'#{T} {b}')