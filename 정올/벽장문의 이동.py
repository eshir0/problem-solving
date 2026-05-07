N = int(input())
a = list(map(int,input().split()))
T = int(input())
m = [int(input()) for i in range(T)]

v = [1] * (N+1)
for i in range(len(a)):
    v[a[i]] = 0

ans = float('inf')

def dfs(n, c):
    global ans

    if c >= ans:
        return
    if n == T:
        ans = min(ans, c)
        return

    x = m[n]

    open = []
    for i in range(1, N+1):
        if v[i] == 0:
            open.append(i)

    d1,d2 = open[0], open[1]

    if x == d1 or x == d2:
        dfs(n+1, c)
        return
    
    v[d1] = 1
    v[x] = 0
    dfs(n+1, c+abs(d1-x))
    v[x] = 1
    v[d1] = 0

    v[d2] = 1
    v[x] = 0
    dfs(n+1, c+abs(d2-x))
    v[x] = 1
    v[d2] = 0

dfs(0,0)
print(ans)