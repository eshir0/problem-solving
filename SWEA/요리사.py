for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for _ in range(N)]

    ans = 1e9
    
    v = [False] * N


    def dfs(n,cnt):
        global ans

        if cnt == N // 2:
            A,B = [],[]
            for i in range(N):
                if v[i]:
                    A.append(i)
                else:
                    B.append(i)

            a,b = 0,0

            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    a += m[A[i]][A[j]] + m[A[j]][A[i]]
            
            for i in range(len(B)):
                for j in range(i+1, len(B)):
                    b += m[B[i]][B[j]] + m[B[j]][B[i]]

            S = abs(a-b)

            if S < ans:
                ans = S

            return
        
        if n == N:
            return
        
        v[n] = True
        dfs(n+1,cnt+1)
        v[n] = False
        dfs(n+1,cnt)
    
    dfs(0,0)
    print(f'#{T} {ans}')