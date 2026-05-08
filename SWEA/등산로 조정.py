for T in range(1,int(input())+1):
    N, K = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(N)]

    # 제일 큰 등산로 값 찾기
    a = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] > a:
                a = m[i][j]

    # 찾은 값에 위치들 찾기
    q = []
    for i in range(N):
        for j in range(N):
            if a == m[i][j]:
                q.append((i,j))

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = 0
    v = [[False] * N for _ in range(N)]

    def dfs(y,x,k,cost):
        global ans
        
        # 정답 갱신
        ans = max(ans,cost)

        # 모든 경우의 수의 방향에서 하기 위함.
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N:  
                
                # 현재 위치의 높이보다 낮은지 확인
                if m[ny][nx] < m[y][x] and not v[ny][nx]:

                    v[ny][nx] = True
                    dfs(ny, nx, k, cost + 1)
                    v[ny][nx] = False

                # 현재 위치보다 높지만 높이를 깍으면 낮은지 확인
                elif (m[ny][nx] - K) < m[y][x] and k > 0 and not v[ny][nx]:

                    v[ny][nx] = True
                    
                    # 현재 위치의 값보다 낮게 깍기
                    f = m[ny][nx]
                    m[ny][nx] = m[y][x] - 1

                    dfs(ny, nx,k-1, cost + 1)

                    m[ny][nx] = f
                    v[ny][nx] = False

    # 높은 등상로의 모든 경우의 수
    for y,x in q:
        v[y][x] = True
        dfs(y, x, 1, 1)
        v[y][x] = False

    print(f'#{T} {ans}')