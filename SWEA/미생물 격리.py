for T in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(K)]

    dy = [0,-1,1,0,0]
    dx = [0,0,0,-1,1]

    # 방향 반전
    rev_d = {1: 2, 2: 1, 3: 4, 4: 3}

    for _ in range(M):
        # 현재 턴에 이동한 미생물을 기록할 임시 딕셔너리
        # Key : (y, x) 좌표 / Value: [총 미생물 수, 가장 큰 미생물 수, 방향]
        c = {}

        for y, x, n, d in m:
            ny = y + dy[d]
            nx = x + dx[d]

            if ny == 0 or nx == 0 or ny == N - 1 or nx == N - 1:
                n //= 2
                d = rev_d[d]

            if n == 0:
                continue

            # 이동할 위치에 이미 다른 미생물이 도착해 있는 경우 (병합)
            if (ny, nx) in c:
                c[(ny, nx)][0] += n # 총 마리 수(누적)

                # 지금 도착한 미생물이 기존 최고 크기의 미생물보다 크면
                if n > c[(ny, nx)][1]:
                    c[(ny, nx)][1] = n # 최고 크기 갱신
                    c[(ny, nx)][2] = d # 방향 new 갱신
            
            # 빈 공간에 처음 도착한 경우
            else:
                c[(ny, nx)] = [n, n, d]
        
        m = [] # 새로운 미생물 리스트를 담을 빈 상자
        
        # c.items()는 key(좌표)와 Value(정보)를 동시에 꺼내줌.
        for (y,x), val in c.items():
            total = val[0] # 합쳐진 총 마리수
            dir = val[2] # 살아남은 최종 방향

            # 새로운 미생물 정보를 리스트에 담기
            m.append([y, x, total, dir])

    ans = sum(n for y, x, n ,d in m)
    print(f'#{T} {ans}')