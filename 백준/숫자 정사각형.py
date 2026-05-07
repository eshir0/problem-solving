N,M = map(int,input().split())
m = [list(map(int,input())) for i in range(N)]

size = min(N,M)

for k in range(size,0,-1):
    for i in range(N - k + 1):
        for j in range(M - k +1):
            if m[i][j] == m[i][j+k-1] == m[i+k-1][j] == m[i+k-1][j+k-1]:
                print(k*k)
                exit()