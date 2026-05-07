N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# + - * /

max_ = -1e9
min_ = 1e9

def dfs(n, total):
    global max_, min_
    if n == N:
        if total > max_:
            max_ = total
        if total < min_:
            min_ = total
        return
    
    for i in range(4):
        if B[i] > 0:
            B[i] -= 1
            
            if i == 0:
                dfs(n+1, total + A[n])
            elif i == 1:
                dfs(n+1, total - A[n])
                pass
            elif i == 2:
                dfs(n+1, total * A[n])
                pass
            elif i == 3:
                dfs(n+1, int(total / A[n]))
                pass

            B[i] += 1

dfs(1,A[0])
print(int(max_))
print(int(min_))