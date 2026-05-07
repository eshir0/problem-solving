N,M = map(int,input().split())
r,c,d = map(int,input().split())
m = [list(map(int,input().split())) for I in range(N)]

# d => 0: 북, 1: 동, 2: 남, 3: 서

dr = [-1,0,1,0]
dc = [0,1,0,-1]

ans = 0

while True:

    if m[r][c] == 0:
        m[r][c] = 2
        ans += 1

    C = True
    
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if m[nr][nc] == 0:
            r, c = nr, nc
            C = False
            break
    if C:
        b = (d + 2) % 4
        br = r + dr[b]
        bc = c + dc[b]

        if m[br][bc] == 1:
            break
        else:
            r, c = br, bc
print(ans)