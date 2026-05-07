for T in range(1,int(input())+1):
    N, K = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(N)]

    max_ = 0
    for i in range(N):
        for j in range(N):
            max_ = max(max_,m[i][j])
    
    q = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == max_:
                q.append((i,j))

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    
    v = [[False] * N for _ in range(N)]

    ans = 0
    def dfs(y,x,l,k):
        global ans

        if l > ans:
            ans = l

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:

                if m[ny][nx] < m[y][x]:

                    v[ny][nx] = True
                    dfs(ny,nx,l+1,k)
                    v[ny][nx] = False

                if k == 1 and m[ny][nx] >= m[y][x] and m[y][x] > m[ny][nx] - K and not v[ny][nx]:
                    
                    tmp = m[ny][nx]
                    
                    v[ny][nx] = True
                    m[ny][nx] = m[y][x] - 1
                    
                    dfs(ny,nx,l+1,k=0)
                    
                    m[ny][nx] = tmp
                    v[ny][nx] = False

    for y,x in q:
        v[y][x] = True
        dfs(y,x,0,1)
        v[y][x] = False

    print(f'#{T} {ans+1}')