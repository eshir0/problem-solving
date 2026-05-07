a = int(input())
for c in range(1, a+1):
    N,M = map(int,input().split())
    m = [list(map(int,input())) for _ in range(N)]

    l = 0
    for i in range(N):
        for j in range(M-1,0,-1):
             if m[i][j] == 1:
                l = m[i][j-55:j+1]
                break
        if l != 0:
            break

    l = ''.join(str(i) for i in l)

    d = {
        '0001101' : 0,
        '0011001' : 1,
        '0010011' : 2,
        '0111101' : 3,
        '0100011' : 4,
        '0110001' : 5,
        '0101111' : 6,
        '0111011' : 7,
        '0110111' : 8,
        '0001011' : 9
    }

    r = []
    for i in range(0,56,7):
        p = l[i:i+7]
        number = d[p]
        r.append(number)
    b = (r[0] + r[2] + r[4] + r[6]) * 3 + r[1] + r[3] + r[5] + r[7]
    if b % 10 == 0:
        o = sum(r)
        print(f'#{c} {o}')
    else:
        print(f'#{c} 0')