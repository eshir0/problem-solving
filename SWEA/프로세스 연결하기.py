for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    e = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1 and 0 < i < N-1 and 0 < j < N-1:
                e.append((i,j))

    dy = [0,0,1,-1]
    dx = [-1,1,0,0]
    
    max_cnt = 0
    min_cost = 1e9


    def dfs(n,m, cost,cnt):
        global max_cnt, min_cost

        if n == len(e):
            if cnt > max_cnt:
                max_cnt = cnt
                min_cost = cost
            elif cnt == max_cnt:
                if min_cost > cost:
                    min_cost = cost
            return
        
        y,x = e[n]

        for i in range(4):
            cp = [i[:] for i in m]
            a = 0
            ny,nx = y,x
            v = False
            
            while True:
                ny += dy[i]
                nx += dx[i]
                if ny < 0 or nx < 0 or ny >= N or nx >= N:
                    v = True
                    break
                if cp[ny][nx] == 1:
                    break
                cp[ny][nx] = 1
                a += 1

            if v == True:
                dfs(n+1,cp,cost + a,cnt+1)
        dfs(n+1,m,cost,cnt)

    dfs(0,m,0,0)
    print(f'#{T} {min_cost}')