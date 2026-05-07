# 1
from collections import deque

N,M = map(int,input().split())
m = [list(map(int,input())) for i in range(N)]

v = [[[0]*2 for _ in range(M)] for _ in range(N)]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs():
    
    q = deque()
    q.append((0,0,0))
    v[0][0][0] = 1
    
    while q:
        y,x,w = q.popleft()
        
        if y == N - 1 and x == M -1:
            return v[y][x][w]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<N and 0<=nx<M:
            
                if m[ny][nx] == 0 and v[ny][nx][w] == 0:
                    v[ny][nx][w] = v[y][x][w] + 1
                    q.append((ny,nx,w))
                    
                elif m[ny][nx] == 1 and w == 0:
                    v[ny][nx][1] = v[y][x][0] +1
                    q.append((ny,nx,1))
    return -1
print(bfs())

# 2
from collections import deque
N,M,K = map(int,input().split())
m = [list(map(int,input())) for _ in range(N)]

v = [[[0] *(K+1) for i in range(M)] for j in range(N)]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs():
    
    q = deque([(0,0,0)])
    v[0][0][0] = 1
    while q:
        y,x,w = q.popleft()
        if y == N-1 and x == M-1:
            return v[y][x][w]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if m[ny][nx] == 0 and v[ny][nx][w] == 0:
                    v[ny][nx][w] = v[y][x][w] + 1
                    q.append((ny,nx,w))
                elif m[ny][nx] == 1 and w < K and v[ny][nx][w+1] == 0:
                    v[ny][nx][w+1] = v[y][x][w] + 1
                    q.append((ny,nx,w+1))
    return -1
print(bfs())

# 3
# 4