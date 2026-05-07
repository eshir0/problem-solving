m = [list(map(int,input().split())) for i in range(9)]
b = []
for i in range(9):
    for j in range(9):
        if m[i][j] == 0:
            b.append((i,j))

def ck(y,x,s):

    for i in range(9):
        if m[y][i] == s or m[i][x] == s:
            return False
        
    Y = (y//3)*3
    X = (x//3)*3
    for i in range(3):
        for j in range(3):
            if m[Y+i][X+j] == s:
                return False
    return True            

def dfs(n):

    if n == len(b):
        for row in m:
            print(*row)
        exit()
    
    y,x = b[n]

    for s in range(1, 10):
        if ck(y,x,s):
            m[y][x] = s
            dfs(n+1)
            m[y][x] = 0

print()
dfs(0)