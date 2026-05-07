from collections import deque

N,M = map(int,input().split())
m = [list(map(int,input())) for i in range(N)]



def bfs(Y,X):
    q = deque([(Y,X)])

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    while q:
        ny,nx = q.popleft()

        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]
            
            if 0 <= y < N and 0 <= x < M:
                if m[y][x] == 1:
                    m[y][x] = m[ny][nx] + 1
                    q.append((y,x))
    return m[N-1][M-1]

r = bfs(0,0)
print(r)