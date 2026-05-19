from collections import deque
for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    v = [[False] * N for i in range(N)]
    
    dy = [0,1]
    dx = [1,0]

    q = deque()
    ans = []
    ans1 = 0

    for i in range(N):
        for j in range(N):
            if m[i][j] > 0 and not v[i][j]:
                
                a,b = 1,1
                for d in range(2):
                    ny,nx = i,j
                    while True:
                        ny += dy[d]
                        nx += dx[d]
                        if 0 <= ny < N and 0 <= nx < N and m[ny][nx] > 0 and dx[d] == 1:
                            b += 1
                        elif 0 <= ny < N and 0 <= nx < N and m[ny][nx] > 0 and dy[d] == 1:
                            a += 1
                        elif 0 <= ny < N and 0 <= nx < N and m[ny][nx] == 0 and dx[d] == 1:
                            break
                        else:
                            break
                            

                ans.append([a,b])
                ans1 += 1
                q.append((i,j))
                v[i][j] = True
                while q:
                    y,x = q.popleft()
                    for d in range(2):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N and not v[ny][nx] and m[ny][nx] > 0:
                            v[ny][nx] = True
                            q.append((ny,nx))
            
    
    print(f'#{T} {ans1}', end=' ')
    c = []
    for a,b in ans:
        c.append((a*b,a,b))
    c.sort()
    for k,a,b in c:
        print(a, b, end=' ')
    print()