for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    v = [False] * N
    ans = 0

    def dfs(n,cost):
        global ans
        if (cost*100) <= ans:
            return
        
        if n == N:
            ans = cost*100
            return
        
        for i in range(N):
            if not v[i]:
                a = 0
                v[i] = True
                a = m[n][i] / 100
                dfs(n+1,cost * a)
                v[i] = False
    dfs(0,1)
    print(f'#{T} {ans:.6f}')