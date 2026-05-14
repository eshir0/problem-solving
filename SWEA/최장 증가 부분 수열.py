for T in range(1,int(input())+1):
    N = int(input())
    A = list(map(int,input().split()))

    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f'#{T} {max(dp)}')