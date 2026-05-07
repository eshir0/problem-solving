N = int(input())
row = [0] * N
a = 0

def ck(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def dfs(x):

    global a

    if x == N:
        a +=1
        return
    
    for i in range(N):
        row[x] = i

        if ck(x):
            dfs(x+1)

dfs(0)
print(a)