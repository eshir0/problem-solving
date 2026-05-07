from collections import deque
for T in range(1,int(input())+1):
    N,W,H = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(H)]

    p = []

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = 1e9

    def dfs(level):
        global ans

        if level == N:
            cp = [row[:] for row in m]
            
            # 찾은 구슬 위치를 통한 시작
            for col in p:
                for i in range(H):
                    if cp[i][col] > 0:
                        
                        q = deque([(i, col, cp[i][col])])
                        cp[i][col] = 0

                        # 벽돌 연쇄반응 코드
                        while q:
                            y,x,power = q.popleft()
                            if power == 1:
                                continue

                            for d in range(4):
                                for k in range(1,power):
                                    ny = y + dy[d] * k
                                    nx = x + dx[d] * k

                                    if 0 <= ny < H and 0 <= nx < W and cp[ny][nx] > 0:
                                        q.append((ny,nx,cp[ny][nx]))
                                        cp[ny][nx] = 0
                        break
                
                # 남아있는 벽돌 떨어지는 중력 코드
                for c in range(W):
                    z = []
                    for r in range(H):
                        if cp[r][c] > 0:
                            z.append(cp[r][c])
                            cp[r][c] = 0

                    row_idx = H -1
                    while z:
                        cp[row_idx][c] = z.pop()
                        row_idx -= 1

            # 남아있는 벽돌 세기 (답 갱신)
            b = 0
            for i in range(H):
                for j in range(W):
                    if cp[i][j] > 0:
                        b += 1
            ans = min(ans,b)       
            return
        
        # 떨어트릴 모든 구슬들의 위치
        for i in range(W):
            p.append(i)
            dfs(level + 1)
            p.pop()
    dfs(0)

    print(f'#{T} {ans}')