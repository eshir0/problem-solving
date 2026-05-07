for O in range(1,int(input())+1):
    N,K = map(int,input().split())
    m = [list(input()) for i in range(N)]

    _y, _x = 0,0
    for i in range(N):
        for j in range(N):
            if m[i][j] == "X":
                _y, _x = i,j

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    v = [[[-1] * 4 for _ in range(N)] for _ in range(N)]

    q = []
    q.append((_y,_x,K,0,0))
    v[_y][_x][0] = K

    ans = -1

    while q:
        y,x,k,d,cost = q.pop(0)

        if m[y][x] == "Y":
            ans = cost
            break

        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < N and 0 <= nx < N:
            if m[ny][nx] != "T":
                if v[ny][nx][d] < k:
                    v[ny][nx][d] = k
                    q.append((ny,nx,k,d,cost+1))
            elif m[ny][nx] == "T" and k > 0:
                if v[ny][nx][d] < k - 1:
                    v[ny][nx][d] = k -1
                    q.append((ny,nx,k-1,d,cost+1))

        l = (d + 3) % 4
        if v[y][x][l] < k:
            v[y][x][l] = k
            q.append((y,x,k,l,cost + 1))
        r = (d + 1) % 4
        if v[y][x][r] < k:
            v[y][x][r] = k
            q.append((y,x,k,r,cost+1))
    print(f'#{O} {ans}')