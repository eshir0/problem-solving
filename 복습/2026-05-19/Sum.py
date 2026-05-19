for T in range(10):
    tc = int(input())
    m = [list(map(int,input().split())) for i in range(100)]

    ans = 0
    z = 0
    for i in range(100):
        x = 0
        y = 0
        for j in range(100):
            x += m[i][j]
            y += m[j][i]
        z += m[i][i]
        r = max(y,x)
        ans = max(ans,r)
    ans = max(ans,z)

    z = 0
    for i in range(99,-1,-1):
        z += m[i][99-i]

    ans = max(ans,z)
    print(f'#{tc} {ans}')