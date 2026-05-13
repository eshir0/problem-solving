for T in range(1,int(input())+1):
    num = list(map(int,input().split()))
    N = num[0]

    ans = 1e9

    def dfs(n,cnt):
        global ans
        
        if ans <= cnt:
            return
        
        if n >= N:
            ans = min(ans,cnt)
            return

        b = num[n]
        for i in range(n + 1, n + b + 1):
            dfs(i, cnt + 1)

    dfs(1,-1)
    print(f'#{T} {ans}')