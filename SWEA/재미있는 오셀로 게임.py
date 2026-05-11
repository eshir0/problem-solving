for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    m = [[0] * N for i in range(N)]

    m[N//2-1][N//2-1] =  2
    m[N//2-1][N//2] =  1
    m[N//2][N//2-1] =  1
    m[N//2][N//2] =  2

    dy = [0,0,-1,1,-1,1,-1,1]
    dx = [-1,1,0,0,1,1,-1,-1]

    for i in range(M):

        x,y,n = map(int,input().split())
        y -= 1
        x -= 1

        m[y][x] = n
        for j in range(8):
            ny,nx = y,x
            temp = []
            while True:
                ny += dy[j]
                nx += dx[j]
            
                if 0 <= ny < N and 0 <= nx < N:
                    if m[ny][nx] == 0:
                        break
                    elif m[ny][nx] != n:
                        temp.append((ny,nx))
                    elif m[ny][nx] == n:
                        for ty, tx in temp:
                            m[ty][tx] = n
                        break
                else:
                    break

    a,b = 0,0
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                a += 1
            elif m[i][j] == 2:
                b += 1

    print(f'#{T} {a} {b}')