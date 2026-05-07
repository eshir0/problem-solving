for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    v = []
    
    dy = [1,1,-1,-1]
    dx = [1,-1,-1,1]
    ans = -1

    def dfs(y,x,cost,dir):
        global ans, a, b

        for i in range(dir, dir + 2):
            if i == 4:
                continue

            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if 0 > ny or 0 > nx or N < ny or N < nx:
                    return
                elif m[ny][nx] not in v:
                    v.append(m[ny][nx])
                    dfs(ny,nx,cost+1,i)
                    v.pop()
                elif i == 3 and a == ny and b == nx:
                    ans = max(ans,cost)
                    break

    for i in range((N+1)//2):
        for j in range(N):
            if i != 0 or j != 0 or i != N-1 or j != N-1:
                a,b = i,j
                v.append(m[i][j])
                dfs(i,j,0,0)
                v.pop()
                
    if (ans+1) == 0:
        print(f'#{T} -1')
    else:
        print(f'#{T} {ans+1}')