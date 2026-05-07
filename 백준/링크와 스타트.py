N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]

R = [sum(i) + sum(j) for i , j in zip(S, zip(*S))]

tot = sum(map(sum, S))

def dfs(n,c,v):
    if n == N:
        if 1<= c <= N - 1:
            return abs(tot - v)
        return int(1e9)
    return min(dfs(n+1, c+1, v+R[n]), dfs(n+1,c,v))

print(dfs(0,0,0))