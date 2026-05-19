for T in range(1,int(input())+1):
    N, M, K = map(int,input().split())

    m = []
    for i in range(K):
        y,x,n,d = map(int,input().split())
        m.append((y,x,n,d))


    dy = [0,-1,1,0,0]
    dx = [0,0,0,-1,1]

    re = {1: 2, 2: 1, 3: 4, 4: 3}

    Map = []
    
    for _ in range(M):

        p = {}

        for y,x,n,d in m:
            ny = y + dy[d]
            nx = x + dx[d]
            
            if ny == 0 or nx == 0 or ny == N-1 or nx == N-1:
                n = n // 2
                d = re[d]
            
            if n == 0:
                continue

            if (ny,nx) not in p:
                p[(ny,nx)] = []
            
            p[(ny,nx)].append((n,d))

        m = []
        for (y,x), n in p.items():
            if len(n) == 1:
                m.append((y,x,n[0][0],n[0][1]))
            
            else:
                total = 0
                k = 0
                max_d = 0

                for num, d in n:
                    total += num
                    if num > k:
                        k = num
                        max_d = d

                m.append((y, x, total, max_d))

    ans = sum(n for y,x,n,d in m)

    print(f'#{T} {ans}')