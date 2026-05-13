for T in range(1,int(input())+1):
    N = int(input())
    M = []
    for i in range(N):
        a,b = map(int,input().split())
        M.append([b,a])
    M.sort()
    
    cnt = 0
    total = 0

    for e, s in M:
        if s >= total:
            cnt += 1
            total = e
            
    print(f'#{T} {cnt}')