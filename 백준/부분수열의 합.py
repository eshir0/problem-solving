N,S = map(int,input().split())
s = list(map(int,input().split()))

a = 0

def dfs(n, total):
    global a
    if n == N:
        if total == S:
            a += 1
        return

    dfs(n+1,total + s[n])
    
    dfs(n+1, total)

dfs(0,0)
if S == 0:
    a -= 1
print(a)