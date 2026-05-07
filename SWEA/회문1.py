for _ in range(1, 11):
    L = int(input())
    m = [list(input()) for i in range(8)]

    c = 0
    
    for i in range(8):
        for j in range(8 -L +1):
            w = m[i][j:j+L]
            if w == w[::-1]:
                c += 1
    for i in range(8-L+1):
        for j in range(8):
            w = ''
            for k in range(L):
                w += m[i+k][j]
            if w == w[::-1]:
                c += 1
                
    print(f"#{_} {c}")