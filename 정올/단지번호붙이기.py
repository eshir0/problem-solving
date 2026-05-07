# BFS 형태 문제 풀이
N = int(input())
m = [list(input()) for i in range(N)]
for i in range(N):
    for j in range(N):
        m[i][j] = int(m[i][j])

v = [[False] * N for _ in range(N)]
a = 0
b = []
dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs():
    global a

    for i in range(N):
        for j in range(N):
            if m[i][j] > 0:
                ans = 0
                ans += 1
                m[i][j] = 0
                a += 1
                q = [(i,j)]
                while q:
                    y,x = q.pop(0)
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N:
                            if m[ny][nx] > 0:
                                if not v[ny][nx]:
                                    v[ny][nx] = True
                                    m[ny][nx] = 0
                                    ans += 1
                                    q.append((ny,nx))
                b.append(ans)
    return
bfs()
b = sorted(b)
print(a,*b, sep='\n')

# DFS 형태 문제 풀이
N = int(input())
m = [list(input()) for i in range(N)]
for i in range(N):
    for j in range(N):
        m[i][j] = int(m[i][j])

v = [[False] * N for O in range(N)]
a = 0
b = []


ans = 0

def dfs(y,x):
    global ans
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if m[ny][nx] == 1:
                m[ny][nx] = 0
                ans += 1
                dfs(ny,nx)

for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            ans = 1
            m[i][j] = 0
            a += 1
            dfs(i,j)
            b.append(ans)
b = sorted(b)
print(a,*b,sep='\n')