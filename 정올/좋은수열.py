N = int(input())

def ck(n):
    l = len(n)
    for i in range(1,l//2+1):
        if n[-i:] == n[-2*i:-i]:
            return False
    return True

def dfs(n):
    if len(n) == N:
        print(n)
        exit()


    for i in '123':
        if ck(n + i):
            dfs(n+i)

dfs('')