from collections import deque
N,M = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]

L = 0
b = []
for i in range(N):
    for j in range(N):
        if m[i][j] == 0:
            L += 1
        elif m[i][j] == 2:
            b.append((i,j))
            
if L==0:
    print(0)
    exit()

dy = [0,0,-1,1]
dx = [-1,1,0,0]
ans = 1e9

S = []

def dfs(st):
    global ans

    if len(S) == M:
        time_map = [[-1]*N for _ in range(N)]
        q = deque()
        
        for y,x in S:
            q.append((y,x))
            time_map[y][x] = 0

        zero = 0
        max_time = 0

        while q:
            y,x = q.popleft()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<=ny<N and 0<=nx<N:
                    if m[ny][nx] != 1 and time_map[ny][nx] == -1:
                        time_map[ny][nx] = time_map[y][x] + 1
                        q.append((ny,nx))

                        if m[ny][nx] == 0:
                            zero += 1
                            max_time = time_map[ny][nx]
        if zero == L:
            ans = min(ans,max_time)
        return
    
    for i in range(st,len(b)):
        S.append(b[i])
        dfs(i+1)
        S.pop()
dfs(0)

if ans == 1e9:
    print(-1)
else:
    print(ans)