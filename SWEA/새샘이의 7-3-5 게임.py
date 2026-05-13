for T in range(1,int(input())+1):
    number = list(map(int,input().split()))

    v = [False] * len(number)

    ans = set()

    def dfs(n,cost):

        if n == 3:
            ans.add(cost)
            return
        
        for i in range(len(number)):
            if not v[i]:
                v[i] = True
                dfs(n+1, cost + number[i])
                v[i] = False
    dfs(0,0)
    ans = sorted(ans,reverse=True)

    print(f'#{T} {ans[4]}')