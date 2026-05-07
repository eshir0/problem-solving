M = int(input())
n = [list(map(int, input())) for _ in range(M)]

def dfs(x,y):

    if x <= -1 or x >= M or y <= -1 or y >=M:
        return 0
    
    if n[x][y] == 1:
        n[x][y] = 0
        c = 1

        c += dfs(x-1,y)
        c += dfs(x+1,y)
        c += dfs(x,y-1)
        c += dfs(x,y+1)
        return c
    
    return 0

cs = []

for i in range(M):
    for j in range(M):
        r = dfs(i,j)
        if r > 0:
            cs.append(r)

cs.sort()
print(len(cs))
for s in cs:
    print(s)