from collections import deque
for _ in range(1,11):
    a = int(input())
    m = [list(map(int,input())) for i in range(16)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    
    q = deque([(1,1)])

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<16 and 0<=nx<16:
                if m[ny][nx] == 0:
                    m[ny][nx] = 2
                    q.append((ny,nx))
                elif m[ny][nx] == 3:
                    m[ny][nx] = 2
                    q.append((ny,nx))
    c = 0
    for i in range(16):
        for j in range(16):
            if m[i][j] == 3:
                c += 1
    if c == 1:
        print(f'#{_}', 0)
    else:
        print(f'#{_}', 1)
        
## 크기를 100으로 올림
from collections import deque
for _ in range(1,11):
    a = int(input())
    m = [list(map(int,input())) for i in range(100)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    
    q = deque([(1,1)])

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<100 and 0<=nx<100:
                if m[ny][nx] == 0:
                    m[ny][nx] = 2
                    q.append((ny,nx))
                elif m[ny][nx] == 3:
                    m[ny][nx] = 2
                    q.append((ny,nx))
    c = 0
    for i in range(100):
        for j in range(100):
            if m[i][j] == 3:
                c += 1
    if c == 1:
        print(f'#{_}', 0)
    else:
        print(f'#{_}', 1)