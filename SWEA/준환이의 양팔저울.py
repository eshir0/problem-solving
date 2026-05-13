P = [1] * 10
for i in range(1,10):
    P[i] = P[i-1] * i * 2

for T in range(1,int(input())+1):
    N = int(input())
    number = list(map(int,input().split()))

    ans = 0
    v = [False] * N

    def dfs(n, l, r):
        global ans

        if r > l:
            return
        
        elif l >= sum(number) / 2:
            ans += P[N - n]
            return
        
        if n == N:
            ans += 1
            return
        
        for i in range(N):
            if not v[i]:
                v[i] = True

                dfs(n+1, l + number[i], r)
                dfs(n+1,l, r + number[i])

                v[i] = False
    
    dfs(0,0,0)
    print(f'#{T} {ans}')