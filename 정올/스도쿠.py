m = [list(map(int,input().split())) for i in range(9)]

e = []
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
box = [[False] * 10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if m[i][j] == 0:
            e.append((i,j))
        else:
            num = m[i][j]
            row[i][num] = True
            col[j][num] = True
            idx = (i//3) * 3 + (j//3)
            box[idx][num] = True

def dfs(n):

    if n == len(e):
        for i in m:
            print(*i)
        exit()

    y,x = e[n]
    idx = (y//3) * 3 + (x // 3)

    for s in range(1,10):
        if not row[y][s] and not col[x][s] and not box[idx][s]:
            row[y][s] = col[x][s] = box[idx][s] = True
            m[y][x] = s
            dfs(n+1)
            row[y][s] = col[x][s] = box[idx][s] = False
            m[y][x] = 0
dfs(0)