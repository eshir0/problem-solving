for T in range(1,int(input())+1):
    m = [list(input().split()) for i in range(4)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = set()
    
    def dfs(n,y,x,run1):
        
        if n == 6:
            ans.add(run1)
            return
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4:
                dfs(n+1,ny,nx,run1+m[ny][nx])
                dfs(n+1,ny,nx,run1+m[ny][nx])
    
    for i in range(4):
        for j in range(4):
            dfs(0,i,j,m[i][j])
    
    print(f'#{T} {len(ans)}')