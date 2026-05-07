from collections import deque

X,Y = map(int,input().split())
m = [list(map(int,input().split())) for i in range(Y)]

q = deque()

for i in range(Y):
    for j in range(X):
        if m[i][j] == 1:
            q.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
while q:
    y,x = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if 0 <= ny < Y and 0 <= nx < X:
            if m[ny][nx] == 0:
                m[ny][nx] = m[y][x] + 1
                q.append((ny,nx))
ans = 0

for i in range(Y):
    for j in range(X):
        if m[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans,m[i][j])
print(ans-1)