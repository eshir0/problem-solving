# DFS를 쓴 풀이 (내 풀이)
for T in range(1,int(input())+1):
    B = list(map(int,input().split()))
    N = list(map(int,input().split()))

    ans = B[3]

    def dfs(n,cost):
        global ans

        if cost >= ans:
            return
        
        if n >= 12:
            ans = cost
            return
        
        dfs(n+1,cost + (N[n] * B[0]))
        dfs(n+1, cost + B[1])
        dfs(n+3, cost + B[2])
            
    dfs(0,0)
    print(f'#{T} {ans}')

# DP를 쓴 풀이 (다른사람 풀이)
if __name__ == "__main__":
 
    T = int(input())
 
    for tc in range(1, T + 1):
        day, month, three_month, year = map(int, input().split())
 
        plan = [0] + list(map(int ,input().split()))
        dp = [0] * 13
 
        for i in range(1, 13):
            dp[i] = dp[i - 1] + min(plan[i] * day, month)
 
            if i >= 3:
                dp[i] = min(dp[i], dp[i - 3] + three_month)
        
        answer = min(dp[12], year)
        print(f"#{tc} {answer}")