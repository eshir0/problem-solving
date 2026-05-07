from collections import deque

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = []
for i in range(N):
    for j in range(M):
        if m[i][j] == 0:
            empty.append((i, j))

ans = 0 # 최대 안전 영역의 크기를 저장할 변수

def dfs(start, count):
    global ans
    
    # [시뮬레이션 시작] 벽 3개를 다 세웠다면?
    if count == 3:
        # 🚨 핵심 1. 원본 지도를 망가뜨리지 않기 위해 '복사본'을 만듭니다.
        temp_m = [row[:] for row in m]

        # 🚨 핵심 2. 큐도 매번 새로 만들어서 초기 바이러스 위치를 세팅합니다.
        q = deque()
        for i in range(N):
            for j in range(M):
                if temp_m[i][j] == 2:
                    q.append((i, j))

        # 3. '복사본 지도(temp_m)'에서 바이러스를 퍼뜨립니다.
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < N and 0 <= nx < M:
                    if temp_m[ny][nx] == 0:
                        temp_m[ny][nx] = 2 # 원본이 아닌 복사본을 감염시킵니다!
                        q.append((ny, nx))        
        
        # 4. 바이러스가 다 퍼진 후, 남아있는 안전 영역(0)의 개수를 셉니다.
        safe_count = 0
        for i in range(N):
            for j in range(M):
                if temp_m[i][j] == 0:
                    safe_count += 1
                    
        # 5. 기존 최댓값과 비교하여 더 큰 값으로 갱신합니다.
        ans = max(ans, safe_count)
        return
    
    # [벽 세우기]
    for i in range(start, len(empty)):
        y, x = empty[i]

        m[y][x] = 1
        dfs(i + 1, count + 1)
        m[y][x] = 0

# 0번째 빈칸부터, 벽 0개 세운 상태로 탐색 시작
dfs(0, 0)
print(ans)