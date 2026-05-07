a = int(input())
for c in range(1,a+1):
    n, s = input().split()

    n = list(n)
    s = int(s)

    m = 0
    v = set()

    def dfs(c):
        global m

        if c == s:
            m = max(m,int("".join(n)))
            return
        
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                n[i], n[j] = n[j],n[i]

                C = "".join(n)

                if (C, c+1) not in v:
                    v.add((C, c+1))
                    dfs(c+1)
                n[i],n[j] = n[j],n[i]
    dfs(0)
    print(f'#{c} {m}')