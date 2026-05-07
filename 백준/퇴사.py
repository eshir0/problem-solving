N = int(input())
T = [0] * (N +1)
P = [0] * (N +1)

for i in range(1, N+1):
    T[i], P[i] = map(int,input().split())

dp = [0] * (N+2)

for i in range(N, 0, -1):
    if i + T[i] <= N+1:
        dp[i] = max(dp[i+1],P[i] + dp[i+T[i]])

    else:
        dp[i] = dp[i+1]
print(dp[1])