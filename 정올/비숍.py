N,M = map(int,input().split())
m = [list(map(int,input().split())) for i in range(N)]

a = []
for i in range(N):
    for j in range(M):
        if m[i][j] != 0 and m[i][j] != 6:
            a.append((i,j,m[i][j]))

dy = [0,0,-1,1]
dx = [-1,1,0,0]
ans = 1e9

def dfs(n,m):

    global ans

    if n == len(a):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if m[i][j] == 0:
                    cnt += 1
        ans = min(ans,cnt)
        return
    
    y,x,s = a[n]

    if s == 1:
        for dir in range(4):
            cp = [i[:] for i in m]
            ny, nx = y,x    
            while True:
                ny += dy[dir]
                nx += dx[dir]
                if 0 <= ny < N and 0 <= nx < M and m[ny][nx] != 6:
                    if cp[ny][nx] == 0:
                        cp[ny][nx] = 1
                    elif cp[ny][nx] > 0 and cp[ny][nx] != 6:
                        pass
                else:
                    break
        dfs(n+1,cp)
    if s == 2:
        for dir in [[0,2],[1,3]]:
            cp = [i[:] for i in m]
            for d in dir:
                ny, nx = y,x    
                while True:
                    ny += dy[d]
                    nx += dx[d]
                    if 0 <= ny < N and 0 <= nx < M and m[ny][nx] != 6:
                        if cp[ny][nx] == 0:
                            cp[ny][nx] = 1
                        elif cp[ny][nx] > 0 and cp[ny][nx] != 6:
                            pass
                    else:
                        break
            dfs(n+1,cp)
    if s == 3:
        for dir in [[0,1],[1,2],[2,3],[3,0]]:
            cp = [i[:] for i in m]
            for d in dir:
                ny, nx = y,x    
                while True:
                    ny += dy[d]
                    nx += dx[d]
                    if 0 <= ny < N and 0 <= nx < M and m[ny][nx] != 6:
                        if cp[ny][nx] == 0:
                            cp[ny][nx] = 1
                        elif cp[ny][nx] > 0 and cp[ny][nx] != 6:
                            pass
                    else:
                        break
            dfs(n+1,cp)
    if s == 4:
        for dir in [[0,1,2],[1,2,3],[2,3,0],[3,0,1]]:
            cp = [i[:] for i in m]
            for d in dir:
                ny, nx = y,x    
                while True:
                    ny += dy[d]
                    nx += dx[d]
                    if 0 <= ny < N and 0 <= nx < M and m[ny][nx] != 6:
                        if cp[ny][nx] == 0:
                            cp[ny][nx] = 1
                        elif cp[ny][nx] > 0 and cp[ny][nx] != 6:
                            pass
                    else:
                        break
            dfs(n+1,cp)
    if s == 5:
        cp = [i[:] for i in m]
        for dir in range(4):
            
            ny, nx = y,x    
            while True:
                ny += dy[dir]
                nx += dx[dir]
                if 0 <= ny < N and 0 <= nx < M and m[ny][nx] != 6:
                    if cp[ny][nx] == 0:
                        cp[ny][nx] = 1
                    elif cp[ny][nx] > 0 and cp[ny][nx] != 6:
                        pass
                else:
                    break
        dfs(n+1,cp)
dfs(0,m)
print(ans)