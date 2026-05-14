# 직접 만든 코드 (도움 x)
for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    Map = [list(map(int,input().split())) for i in range(N)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    Dy = [1,1,-1,-1]
    Dx = [-1,1,-1,1]
    ans = 0

    def ck(sy,sx):
        global ans

        
        
        cost1 = Map[sy][sx]
        
        y,x = sy,sx
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                cost1 += Map[ny][nx]
                for j in range(M-2):
                    ny += dy[i]
                    nx += dx[i]
                    if 0 <= ny < N and 0 <= nx < N:
                        cost1 += Map[ny][nx]
                    else:
                        break

        cost2 = Map[sy][sx]
    
        y,x = sy,sx
        for i in range(4):
            ny = y + Dy[i]
            nx = x + Dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                cost2 += Map[ny][nx]
                for j in range(M-2):
                    ny += Dy[i]
                    nx += Dx[i]
                    if 0 <= ny < N and 0 <= nx < N:
                        cost2 += Map[ny][nx]
                    else:
                        break

        a = max(cost1,cost2)
        ans = max(ans,a)

    for i in range(N):
        for j in range(N):
            ck(i,j)

    print(f'#{T} {ans}')

# ai (단축버전)
for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    Map = [list(map(int,input().split())) for i in range(N)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    Dy = [1,1,-1,-1]
    Dx = [-1,1,-1,1]
    ans = 0

    def ck(sy,sx):
        global ans

        
        
        cost1 = Map[sy][sx]
        
        y,x = sy,sx
        for i in range(4):
            for j in range(1, M):
                ny = y + dy[i] * j
                nx = x + dx[i] * j
                if 0 <= ny < N and 0 <= nx < N:
                    cost1 += Map[ny][nx]
                else:
                    break

        cost2 = Map[sy][sx]
    
        y,x = sy,sx
        for i in range(4):
            for j in range(1, M):
                ny = y + Dy[i] * j
                nx = x + Dx[i] * j
                if 0 <= ny < N and 0 <= nx < N:
                    cost2 += Map[ny][nx]
                else:
                    break

        a = max(cost1,cost2)
        ans = max(ans,a)

    for i in range(N):
        for j in range(N):
            ck(i,j)

    print(f'#{T} {ans}')