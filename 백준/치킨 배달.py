N,M = map(int,input().split())
m = [list(map(int,input().split())) for i in range(N)]

a = []
b = []

for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            a.append((i,j))
        elif m[i][j] == 2:
            b.append((i,j))
            m[i][j] = 0

ans = float('inf')
chkin = []

def dfs(idx,count):
    global ans

    if count == M:
        total = 0

        for ny,nx in a:
            d = float('inf')
            for cy, cx in chkin:
                d = min(d,abs(ny - cy) + abs(nx - cx))
            total += d
        ans = min(ans, total)
        return
    
    for i in range(idx, len(b)):
        chkin.append(b[i])
        dfs(i + 1, count + 1)
        chkin.pop()
dfs(0,0)
print(ans)