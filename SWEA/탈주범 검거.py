from collections import deque
for T in range(1,int(input())+1):
    N, M, R, C, L = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(N)]

    q = deque([(R,C,1)])
    
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ck = {1: [0,1,2,3], 2 : [2,3], 3: [0,1], 4:[2,1], 5 : [3,1], 6 : [0,3] , 7 : [0,2]}

    v = [[False] * M for _ in range(N)]
    v[R][C] = True

    ans = 0

    while q:
        y,x,c = q.popleft()

        r = m[y][x]
        m[y][x] = 8
        if c == L:
            continue

        if r == 1:
            for i in ck[r]:
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    if dy[i] == -1:
                        if m[ny][nx] in [1,2,5,6]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dy[i] == 1:
                        if m[ny][nx] in [1,2,4,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dx[i] == -1:
                        if m[ny][nx] in [1,3,4,5]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dx[i] == 1:
                        if m[ny][nx] in [1,3,6,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
        elif r == 2:
            for i in ck[r]:
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    if dy[i] == -1:
                        if m[ny][nx] in [1,2,5,6]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dy[i] == 1:
                        if m[ny][nx] in [1,2,4,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
        elif r == 3:
            for i in ck[r]:
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    if dx[i] == -1:
                        if m[ny][nx] in [1,3,4,5]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dx[i] == 1:
                        if m[ny][nx] in [1,3,6,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
        elif r == 4:
            for i in ck[r]:
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    if dy[i] == -1:
                        if m[ny][nx] in [1,2,5,6]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dx[i] == 1:
                        if m[ny][nx] in [1,3,6,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
        elif r == 5:
            for i in ck[r]:
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    if dy[i] == 1:
                        if m[ny][nx] in [1,2,4,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dx[i] == 1:
                        if m[ny][nx] in [1,3,6,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
        elif r == 6:
            for i in ck[r]:
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    if dy[i] == 1:
                        if m[ny][nx] in [1,2,4,7]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dx[i] == -1:
                        if m[ny][nx] in [1,3,4,5]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
        elif r == 7:
            for i in ck[r]:
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and not v[ny][nx]:
                    if dy[i] == -1:
                        if m[ny][nx] in [1,2,5,6]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
                    elif dx[i] == -1:
                        if m[ny][nx] in [1,3,4,5]:
                            v[ny][nx] = True
                            ans += 1
                            q.append((ny,nx,c+1))
    print(f'#{T} {ans+1}')

# ai가 만든 코드
for T in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]

    # 1. 방향 및 사전(Dictionary) 세팅 🛠️
    # 0:상, 1:하, 2:좌, 3:우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # 반대 방향 매칭 (상<->하, 좌<->우)
    rev_dir = {0: 1, 1: 0, 2: 3, 3: 2}
    
    # 파이프 번호별 뚫려있는 방향
    pipes = {
        1: [0, 1, 2, 3], # 상하좌우
        2: [0, 1],       # 상하
        3: [2, 3],       # 좌우
        4: [0, 3],       # 상우
        5: [1, 3],       # 하우
        6: [1, 2],       # 하좌
        7: [0, 2]        # 상좌
    }

    # 2. 방문 배열 및 큐 초기화
    v = [[False] * M for _ in range(N)]
    v[R][C] = True
    ans = 1
    q = [(R, C, 1)]

    # 3. BFS 탐색 시작 🧩
    while q:
        y, x, c = q.pop(0)
        
        # 제한 시간에 도달하면 더 이상 퍼져나가지 않음
        if c == L:
            continue
            
        cur_pipe = m[y][x]
        
        # 현재 파이프에서 갈 수 있는 방향(d)만 쏙쏙 골라서 탐색
        for d in pipes[cur_pipe]:
            ny = y + dy[d]
            nx = x + dx[d]
            
            # 맵 안이고, 방문 안 했고, 파이프가 있다면?
            if 0 <= ny < N and 0 <= nx < M and not v[ny][nx] and m[ny][nx] != 0:
                next_pipe = m[ny][nx]
                
                # 핵심: 다음 칸의 파이프가 '나의 반대 방향(rev_dir[d])'으로 뚫려있는가?
                if rev_dir[d] in pipes[next_pipe]:
                    v[ny][nx] = True
                    ans += 1
                    q.append((ny, nx, c + 1))

    print(f'#{T} {ans}')