for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    # 가로줄 하나의 한개의 수만 더하기 때문
    v = [False] * N
    ans = 1e9

    def dfs(n,cost):
        global ans

        # 가지치기
        if cost >= ans:
            return

        # 세로줄을 다 돌았기 때문에 전부 더한 값을 갱신
        if n == N:
            ans = cost
            return
        
        # 가로줄 하나의 한개의 수를 전부 더한 값 계산
        for i in range(N):
            if not v[i]:
                v[i] = True
                dfs(n+1,cost + m[n][i])
                v[i] = False

    dfs(0,0)
    print(f'#{T} {ans}')