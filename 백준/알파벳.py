R,C = map(int,input().split())
m = [list(input()) for _ in range(R)]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def bfs():
    
    q = set([(0,0,m[0][0])])
    ans = 1
    while q:
        y,x,p = q.pop()
        ans = max(ans,len(p))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<R and 0<=nx<C:
                if m[ny][nx] not in p:
                    q.add((ny,nx,p+m[ny][nx]))
    return ans
print(bfs())