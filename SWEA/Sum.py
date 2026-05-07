for _ in range(10):
    a = int(input())
    m = [list(map(int,input().split())) for i in range(100)]

    s = []
    for i in range(100):
        cx = 0
        cy = 0
        for j in range(100):
            cx += m[i][j]
            cy += m[j][i]
        s.append(cx)
        s.append(cy)
    cx = 0
    for i in range(100):
        cx += m[i][i]
    s.append(cx)
    cx = 0
    for i in range(99,0,-1):
        cx += m[i][i]
    s.append(cx)
    
    print(f'#{a} {max(s)}')