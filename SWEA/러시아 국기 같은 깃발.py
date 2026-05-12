for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    m = [list(input()) for i in range(N)]

    ans = 1e9

    for i in range(0,N - 2):

        for j in range(i + 1, N - 1):
            
            cnt = 0

            for r in range(0, i + 1):
                cnt += M - m[r].count('W')
            for r in range(i+1, j+1):
                cnt += M - m[r].count('B')
            for r in range(j+1, N):
                cnt += M - m[r].count('R')
            
            if cnt < ans:
                ans = cnt
                
    print(f'#{T} {ans}')