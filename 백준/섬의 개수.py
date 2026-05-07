def dfs(x,y):
    
    if x <= -1 or x >= X or y <= -1 or y >= Y:
        return 0
    
    if M[y][x] == 1:
        M[y][x] = 0
        c = 1

        c += dfs(x-1,y)
        c += dfs(x,y-1)
        c += dfs(x+1,y)
        c += dfs(x,y+1)
        c += dfs(x-1,y+1)
        c += dfs(x+1,y-1)
        c += dfs(x+1,y+1)
        c += dfs(x-1,y-1)
        return c
    return 0

while True:
    X,Y = map(int,input().split())
    M = [list(map(int,input().split())) for i in range(Y)]
    c = []    
    if X+Y == 0:
        break
    for i in range(Y):
        for j in range(X):
            r = dfs(j,i)
            if r > 0:
                c.append(r)
    print(len(c))