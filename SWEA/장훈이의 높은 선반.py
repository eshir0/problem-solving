for T in range(1, int(input())+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))

    H = sorted(H)
    v = [False] * N

    ans = 1e9

    def dfs(n,st):
        global ans

        if n >= B:
            ans = min(ans,n)
            return
        
        for i in range(st, N):
            if not v[i]:
                v[i] = True
                dfs(n+H[i], i+1)
                v[i] = False
    dfs(0,0)
    print(f'#{T} {ans - B}')