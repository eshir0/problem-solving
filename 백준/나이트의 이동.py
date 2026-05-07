from collections import deque

def bfs(startY, startX, endY,endX):

    if startY == endY and startX == endX:
        return 0

    q = deque([(startY,startX)])
    m[startY][startX] = 1

    dx = [-2,-2,2,2,-1,1,-1,1]
    dy = [-1,1,-1,1,-2,-2,2,2]

    while q:
        y,x = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < k and 0 <= nx < k:
                if m[ny][nx] == 0:
                    m[ny][nx] = m[y][x] + 1
                    q.append((ny,nx))

                    if ny == endY and nx == endX:
                        return m[ny][nx] - 1
    return 0

n = int(input())
for i in range(n):
    k = int(input())
    m = [[0] * k for _ in range(k)]
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    
    r = bfs(start[1],start[0],end[1],end[0])
    print(r)