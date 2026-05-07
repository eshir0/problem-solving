from collections import deque
for _ in range(10):
    a = int(input())
    m = [list(map(int,input().split())) for i in range(100)]

    e = deque()
    for i in range(100):
        if m[99][i] == 2:
            e.append((99,i))


    dy = [0,0,-1]
    dx = [-1,1,0]

    while e:
        y,x = e.popleft()
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<100 and 0<=nx<100:
                if m[ny][nx] == 1:
                    m[ny][nx] = 2
                    e.append((ny,nx))
                    break
                
    for i in range(100):
        if m[0][i] == 2:
            print(f'#{a} {i}')