for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input())) for _ in range(N)]

    q = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 2:
                q.append((i,j))
                m[i][j] = 4
                break

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    r = 0

    while q:
        y,x = q.pop(0)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if m[ny][nx] == 0:
                    m[ny][nx] = m[y][x] + 1
                    q.append((ny,nx))
                elif m[ny][nx] == 3:
                    m[ny][nx] = m[y][x] + 1
                    r = m[y][x]
                    q.append((ny,nx))

    if r == 0:
        print(f'#{T} 0')
    else:
        print(f'#{T} {r-4}')