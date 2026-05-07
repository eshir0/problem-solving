for tk in range(1,int(input())+1):
    N, L = map(int,input().split())
    T,K = [],[]
    for i in range(N):
        a,b = map(int,input().split())
        T.append(a)
        K.append(b)

    ans = 0

    def dfs(k,t,st):
        global ans

        if k > L:
            return

        if t > ans:
            ans = max(ans,t)
        
        for i in range(st,N):
            t = t + T[i]
            dfs(k+K[i],t,i+1)
            t = t - T[i]

    dfs(0,0,0)
    print(f'#{tk} {ans}')