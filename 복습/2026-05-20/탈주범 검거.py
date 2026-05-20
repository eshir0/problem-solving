from collections import deque
for T in range(1,int(input())+1):
    N, M, R, C ,L = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(N)]

    q = deque([(R,C)])

    v = [[False] * M for i in range(N)]
    v[R][C] = True
    
    cr = {
        1: [(0,-1),(0,1),(-1,0),(1,0)],
        2: [(-1,0),(1,0)],
        3: [(0,-1),(0,1)],
        4: [(-1,0),(0,1)],
        5: [(1,0),(0,1)],
        6: [(0,-1),(1,0)],
        7: [(-1,0),(0,-1)]
    }
    cnt = 1

    for _ in range(L - 1):
        for _ in range(len(q)):
            y,x = q.popleft()
            p = m[y][x]

            for dy,dx in cr[p]:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and m[ny][nx] > 0 and not v[ny][nx]:
                    if (-dy, -dx) in cr[m[ny][nx]]:
                        v[ny][nx] = True
                        q.append((ny,nx))
                        cnt += 1

    print(f'#{T} {cnt}')