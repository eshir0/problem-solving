# bfs 방식
from collections import deque
for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(N)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    
    v = [[False] * N for i in range(N)]
    
    ans = 0

    def bfs(l,r,n,cost):
        global ans, ck

        q = deque([(l,r,1)])

        while q:
            y,x,c = q.popleft()
            if m[y][x] == 1: ck += 1

            if ((ck * M) - (c**2 + (c-1)**2)) >= 0: ans = max(ans,ck)
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not v[ny][nx]:
                    v[ny][nx] = True
                    q.append((ny,nx,c+1))

        
    for i in range(N):
        for j in range(N):
            ck = 0
            v[i][j] = True
            bfs(i,j,0,0)
            v = [[False] * N for i in range(N)]

    print(f'#{T} {ans}')

# 맨해튼 거리 기반 방식
for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 모든 집(1)의 좌표를 리스트에 미리 수집
    houses = [(i, j) for i in range(N) for j in range(N) if m[i][j] == 1]
    ans = 0
    
    # 2. 지도의 모든 칸을 한 번씩 중심점으로 삼기
    for y in range(N):
        for x in range(N):
            # dist_counts[d] = 중심점(y,x)에서 거리가 d인 집의 개수
            dist_counts = [0] * (2 * N + 1) 
            
            for hy, hx in houses:
                # 맨해튼 거리 공식: |y1 - y2| + |x1 - x2|
                dist = abs(y - hy) + abs(x - hx)
                dist_counts[dist] += 1
            
            ck = 0
            # 3. K를 1부터 맵을 다 덮을 때까지 늘려가며 수익 계산
            for k in range(1, 2 * N + 1):
                # 거리가 k-1인 집들을 누적해서 더해줌 (K=1일 때 거리는 0)
                ck += dist_counts[k - 1] 
                cost = k * k + (k - 1) * (k - 1)
                
                # 손해를 보지 않으면 정답 갱신
                if ck * M >= cost:
                    ans = max(ans, ck)

    print(f'#{T} {ans}')