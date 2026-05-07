for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    w = list(reversed(sorted(map(int,input().split()))))
    t = list(reversed(sorted(map(int,input().split()))))

    ans = 0
    for i in range(len(t)):
        while w:
            a = w.pop(0)
            if t[i] >= a:
                ans += a
                break
        if not w:
            break

    if ans == 0:
        print(f'#{T} 0')
    else:
        print(f'#{T} {ans}')