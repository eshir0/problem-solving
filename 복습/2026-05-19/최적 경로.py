for T in range(1,int(input())+1):
    N = int(input())
    m = list(map(int,input().split()))

    xy = []
    for i in range(0,len(m),2):
        xy.append((m[i],m[i+1]))

    start,home = xy.pop(0),xy.pop(0)

    v = [False] * (N+1)
    ans = 1e9
    a = 0

    def dfs(n,cost,x,y):
        global ans ,a

        if cost >= ans:
            return

        if n == N:
            cost += (abs(x-home[0]) + abs(y-home[1]))
            ans = min(ans,cost)
            return
        
        for i in range(N):
            if not v[i]:
                v[i] = True
                a = (abs(x - xy[i][0]) + abs(y - xy[i][1]))
                dfs(n+1, cost + a, xy[i][0], xy[i][1] )
                v[i] = False

    dfs(0,0,start[0],start[1])
    print(f'#{T} {ans}')