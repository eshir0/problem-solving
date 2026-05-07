for T in range(1,int(input())+1):
    N = int(input())
    V = [list(map(int,input().split())) for _ in range(N)]

    v = [False] * N

    ans = 1e9

    def dfs(n,cost):
        global ans, m

        if cost > ans:
            return

        if n == N:
            ans = min(ans,cost)
            return

        for i in range(N):
            if not v[i]:
                v[i] = True
                dfs(n+1,cost + V[n][i])
                v[i] = False
    dfs(0,0)
    print(f'#{T} {ans}')