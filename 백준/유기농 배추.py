# 런타임 에러
def dfs(X,Y):

    if X < 0 or X >= N or Y < 0 or Y >= M:
        return 0
    
    if MAP[Y][X] == 1:
        MAP[Y][X] = 0
        c = 1

        c += dfs(X-1,Y)
        c += dfs(X+1,Y)
        c += dfs(X,Y-1)
        c += dfs(X,Y+1)
        return c
    return 0

k = int(input())
for i in range(k):
    N,M,K = map(int,input().split())
    MAP = [[0] * N for _ in range(M)]
    for j in range(K):
        x,y = map(int,input().split())
        MAP[y][x] = 1
        
    c = []

    for _ in range(M):
        for l in range(N):
            r = dfs(l,_)
            if r > 0:
                c.append(r)
    print(len(c))

####### BFS로 전환

from collections import deque

# ***
def bfs(X,Y):
    q = deque([(X,Y)])
    MAP[Y][X] = 0
    c = 1

    x_ = [-1,1,0,0]
    y_ = [0,0,-1,1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            _x = x + x_[i]
            _y = y + y_[i]

            if 0 <= _x < N and 0 <= _y < M:
                if MAP[_y][_x] == 1:
                    MAP[_y][_x] = 0
                    c +=1
                    q.append((_x,_y))
    return c


k = int(input())
for i in range(k):
    N,M,K = map(int,input().split())
    MAP = [[0] * N for _ in range(M)]
    for j in range(K):
        x,y = map(int,input().split())
        MAP[y][x] = 1
        
    c = []

    for _ in range(M):
        for l in range(N):
            if MAP[_][l] == 1: # ***
                r = bfs(l,_)
                if r > 0:
                    c.append(r)
    print(len(c))