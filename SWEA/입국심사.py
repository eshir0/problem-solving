for T in range(1,int(input())+1):
    N,M = map(int,input().split())
    t = [int(input()) for i in range(N)]
    t = sorted(t)

    l = 1
    r = t[-1] * M
    ans = r

    while l <= r:
        mid = (l+r) // 2
       
        total = 0
        for time in t:
            total += mid // time
        
        if total >= M:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(f'#{T} {ans}')