for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    dy = [1,1,-1,-1]
    dx = [1,-1,-1,1]

    ans = -1
    
    def dfs(sy,sx,y,x,d,r):
        global ans

        if d == 3 and y == sy and x == sx:
            ans = max(ans, len(r))
            return
        
        for i in range(d, d + 2):
            if i >= 4:
                continue

            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if ny == sy and nx == sx and i == 3:
                    dfs(sy,sx,ny,nx,i,r)
                elif m[ny][nx] not in r:
                    r.add(m[ny][nx])
                    dfs(sy,sx,ny,nx,i,r)
                    r.remove(m[ny][nx])

    for i in range(N-2):
        for j in range(1, N-1):
            dfs(i,j,i,j,0,{m[i][j]})

    print(f'#{T} {ans}')