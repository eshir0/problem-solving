from collections import deque
for T in range(1,int(input())+1):
    N = int(input())
    m = [list(input()) for i in range(N)]

    dy = [0,0,-1,1,-1,1,-1,1]
    dx = [-1,1,0,0,1,1,-1,-1]

    v = [[False] * N for i in range(N)]

    def ck(y,x):
        for i in range(8):
            ny =  y + dy[i]
            nx =  x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == "*":
                return False
            
        return True
    
    q = deque()
    ans = 0

    for i in range(N):
        for j in range(N):
            if m[i][j] == "." and not v[i][j] and ck(i,j):
                ans += 1
                q.append((i,j))
                v[i][j] = True

                while q:
                    y, x = q.popleft()
                    v[y][x] = True
                    if ck(y,x):
                        for d in range(8):
                            ny =  y + dy[d]
                            nx =  x + dx[d]
                            if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == "." and not v[ny][nx]:
                                v[ny][nx] = True
                                q.append((ny,nx))

    for i in range(N):
        for j in range(N):
            if not v[i][j] and m[i][j] == ".":
                ans += 1
                v[i][j] = True

    print(f'#{T} {ans}')