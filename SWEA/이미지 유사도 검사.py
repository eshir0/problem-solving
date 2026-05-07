T = int(input())
for _ in range(1,T+1):
    N = int(input())
    a = input()
    b = input()

    dp = [[0] * (N+1) for i in range(N+1)]

    for i in range(N):
        for j in range(N):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                
    ans = dp[N][N]

    c = ans / N * 100
    print(f'#{_} {c:.2f}')