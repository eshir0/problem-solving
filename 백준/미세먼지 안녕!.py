R,C,T = map(int,input().split())
m =[list(map(int,input().split())) for _ in range(R)]

up = -1
down = -1

for i in range(R):
    if m[i][0] == -1:
        up = i
        down = i+1
        break


dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dump(m):

    cp_m = [[0] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):

            if m[y][x] > 0:
                a = m[y][x] // 5
                count = 0

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if 0<=ny<R and 0<=nx<C and m[ny][nx] != -1:
                        cp_m[ny][nx] += a
                        count += 1

                cp_m[y][x] += (m[y][x] -(a*count))
            elif m[y][x] == -1:
                cp_m[y][x] = -1
    return cp_m

def air():
    # 위 공청

    # 왼쪽 면
    for y in range(up -1,0,-1):
        m[y][0] = m[y-1][0]
    # 위쪽 면
    for x in range(0,C-1):
        m[0][x] = m[0][x+1]
    # 오른쪽 면
    for y in range(0,up):
        m[y][C-1] = m[y+1][C-1]
    # 아래쪽 면
    for x in range(C-1, 1,-1):
        m[up][x] = m[up][x-1]
    # 공청 오른쪽
    m[up][1] = 0

    # 아래 공청

    # 왼쪽 면
    for y in range(down + 1, R-1):
        m[y][0] = m[y+1][0]
    # 아래쪽 면
    for x in range(0, C-1):
        m[R-1][x] = m[R-1][x+1]
    # 오른쪽 면
    for y in range(R-1,down,-1):
        m[y][C-1] = m[y-1][C-1]
    # 위쪽 면
    for x in range(C-1,1,-1):
        m[down][x] = m[down][x-1]
    #공청 오른쪽
    m[down][1] = 0

for _ in range(T):
    m = dump(m)
    air()
ans = sum(sum(row) for row in m) + 2
print(ans)