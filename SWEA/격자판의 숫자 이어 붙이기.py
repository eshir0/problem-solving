for T in range(1,int(input())+1):
    m = [list(map(int,input().split())) for _ in range(4)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = set()
    
    def dfs(y,x,n,line):

        if n == 7:
            ans.add(line)
            return
    
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4:
                dfs(ny,nx,n+1,line + str(m[ny][nx]))
    
    for i in range(4):
        for j in range(4):
            dfs(i,j,1, str(m[i][j]))

    print(f'#{T} {len(ans)}')