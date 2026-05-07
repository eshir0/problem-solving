for T in range(1,int(input())+1):
    D, W, K = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(D)]

    ans = 1e9

    def ck():
        for i in range(W):
            p = False
            c = 1
            for j in range(1,D):
                if m[j][i] == m[j-1][i]:
                    c += 1
                else:
                    c = 1
                
                if c >= K:
                    p = True
                    break
            if not p:
                return False
        return True

    def dfs(row,cnt):
        global ans

        if cnt >= ans:
            return

        if row == D:
            if ck():
                ans = cnt
            return

        dfs(row+1,cnt)

        a = m[row][:]
        m[row] = [0] * W
        dfs(row+1,cnt+1)
        m[row] = a

        b = m[row][:]
        m[row] = [1] * W
        dfs(row+1,cnt+1)
        m[row] = b

    dfs(0,0)
    print(f'#{T} {ans}')