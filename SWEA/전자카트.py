for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    v = [False] * N
    v[0] = True
    ans = 1e9

    def dfs(n,y,cost):
        global ans

        if n == N-1:
            ans = min(ans,cost+m[y][0])
            return

        for i in range(N):
            if not v[i]:
                v[i] = True
                dfs(n+1,i,cost + m[y][i])
                v[i] = False

    for i in range(N):
        if not v[i]:
            v[i] = True
            dfs(1,i,m[0][i])
            v[i] = False
            
    print(f'#{T} {ans}')