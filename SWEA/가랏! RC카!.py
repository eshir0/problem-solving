for T in range(1,int(input())+1):
    N = int(input())
    
    ans = 0
    s = 0

    for _ in range(N):
        m = list(map(int,input().split()))

        if m[0] == 1:
            s += m[1]
            ans += s
        elif m[0] == 2:
            if s == 0:
                continue
            s -= m[1]
            ans += s
        elif m[0] == 0:
            ans += s
    
    print(f'#{T} {ans}')