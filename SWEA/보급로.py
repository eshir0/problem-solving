from collections import deque
a = int(input())
for _ in range(1,a+1):
    N = int(input())
    m = [list(map(int,input())) for i in range(N)]


    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    d = [[float('inf')] * N for i in range(N)]
    d[0][0] = 0
    q = deque([(0,0)])


    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if d[y][x] + m[ny][nx] < d[ny][nx]:
                    d[ny][nx] = d[y][x] + m[ny][nx]
                    q.append((ny,nx))
    print(f'#{_} {d[N-1][N-1]}')