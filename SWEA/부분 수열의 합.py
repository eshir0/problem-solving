for T in range(1,int(input())+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    ans = 0

    def dfs(n,num):
        global ans    
        
        if num > K:
            return

        if n == N:
            if num == K:
                ans += 1
            return

        dfs(n + 1 ,num + A[n])
        dfs(n + 1, num)    
  
    dfs(0,0)
    print(f'#{T} {ans}')