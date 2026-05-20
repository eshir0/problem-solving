from collections import deque
for T in range(1,int(input())+1):
    N, W, H = map(int,input().split())
    Map = [list(map(int,input().split())) for i in range(H)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = 1e9
    def dfs(n,m):
        global ans

        if n == N:
            cost = 0
            for i in range(H):
                for j in range(W):
                    if m[i][j] > 0:
                        cost += 1
            ans = min(ans,cost)
            return


        for x in range(W):
            cp = [row[:] for row in m]

            y = -1
            for _ in range(H):
                if cp[_][x] > 0:
                    y = _
                    break

            if y != -1:
                q = deque([(y,x,cp[y][x])])
                cp[y][x] = 0
            
                while q:
                    r, c, p = q.popleft()
                    cp[r][c] = 0
                    if p > 1:
                        for i in range(4):
                            for j in range(1, p):
                                ny = r + dy[i] * j
                                nx = c + dx[i] * j
                                
                                if 0 <= ny < H and 0 <= nx < W:
                                    if cp[ny][nx] > 1:
                                        q.append((ny,nx,cp[ny][nx]))
                                    cp[ny][nx] = 0
            
            
            for c in range(W):
                stack = []
                for r in range(H):
                    if cp[r][c] > 0:
                        stack.append(cp[r][c])
                        cp[r][c] = 0
                r = H - 1
                while stack:
                    cp[r][c] = stack.pop()
                    r -= 1

            dfs(n+1,cp)

    dfs(0,Map)
    print(f'#{T} {ans}')