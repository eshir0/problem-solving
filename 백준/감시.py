N,M = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]

cctv = []

for i in range(N):
    for j in range(M):
        if m[i][j] !=0 and m[i][j] != 6:
            cctv.append((i,j,m[i][j]))

dy = [0,0,-1,1]
dx = [-1,1,0,0]

count = 1e9

def dfs(n,cp):
    global count

    if n == len(cctv):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if cp[i][j] == 0:
                    cnt += 1
        count = min(count, cnt)
        return
    
    y,x,s = cctv[n]

    if s == 1:
        for dir in range(4):
            cp_m = [row[:] for row in cp]

            ny, nx = y,x
            while True:
                ny += dy[dir]
                nx += dx[dir]
                if 0 <= ny < N and 0 <= nx < M and cp_m[ny][nx] != 6:
                    if cp_m[ny][nx] == 0:
                        cp_m[ny][nx] = 1
                    elif cp_m[ny][nx] > 0 and cp_m[ny][nx] != 6:
                        pass
                else:
                    break
            dfs(n+1,cp_m)

    elif s == 2:
        for dir in [[0,1],[2,3]]:
            cp_m = [row[:] for row in cp]
            
            for d in dir:
                ny, nx = y,x
                while True:
                    ny += dy[d]
                    nx += dx[d]
                    if 0 <= ny < N and 0 <= nx < M and cp_m[ny][nx] != 6:
                        if cp_m[ny][nx] == 0:
                            cp_m[ny][nx] = 1
                        elif cp_m[ny][nx] > 0 and cp_m[ny][nx] != 6:
                            pass
                    else:
                        break
            dfs(n+1,cp_m)
    
    elif s == 3:
        for dir in [[2,1],[1,3],[3,0],[0,2]]:
            cp_m = [row[:] for row in cp]

            for d in dir:
                ny, nx = y,x
                while True:
                    ny += dy[d]
                    nx += dx[d]
                    if 0 <= ny < N and 0 <= nx < M and cp_m[ny][nx] != 6:
                        if cp_m[ny][nx] == 0:
                            cp_m[ny][nx] = 1
                        elif cp_m[ny][nx] > 0 and cp_m[ny][nx] != 6:
                            pass
                    else:
                        break
            dfs(n+1,cp_m)
    
    elif s == 4:
        for dir in [[0,1,2],[0,1,3],[2,3,1],[2,3,0]]:
            cp_m = [row[:] for row in cp]

            for d in dir:
                ny, nx = y,x
                while True:
                    ny += dy[d]
                    nx += dx[d]
                    if 0 <= ny < N and 0 <= nx < M and cp_m[ny][nx] != 6:
                        if cp_m[ny][nx] == 0:
                            cp_m[ny][nx] = 1
                        elif cp_m[ny][nx] > 0 and cp_m[ny][nx] != 6:
                            pass
                    else:
                        break
            dfs(n+1,cp_m)
    
    elif s == 5:
        cp_m = [row[:] for row in cp]
        
        for d in range(4):
            ny, nx = y,x
            while True:
                ny += dy[d]
                nx += dx[d]
                if 0 <= ny < N and 0 <= nx < M and cp_m[ny][nx] != 6:
                    if cp_m[ny][nx] == 0:
                        cp_m[ny][nx] = 1                
                    elif cp_m[ny][nx] > 0 and cp_m[ny][nx] != 6:
                        pass
                else:
                    break
        dfs(n+1,cp_m)
dfs(0,m)
print(count)