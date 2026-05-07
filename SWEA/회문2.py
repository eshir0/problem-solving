for _ in range(10):
    a = int(input())
    m = [list(input()) for i in range(100)]

    c = 1
    for i in range(100):
        for l in range(2,101):
            for j in range(100 - l + 1):
                w = m[i][j:j+l]
                if w == w[::-1]:
                    c = max(c,l)
                W = ''
                for k in range(l):
                    W += m[j+k][i]
                if W == W[::-1]:
                    c = max(c,l)
    print(f'#{_+1} {c}')