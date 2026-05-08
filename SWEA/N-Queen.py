for T in range(1,int(input())+1):
    N = int(input())
    
    #가로 체크를 하지 않기 위해
    row = [0] * N
    ans = 0

    # 세로 대각선 체크 함수
    def ck(n):
        for i in range(n):
            if row[n] == row[i] or abs(row[n] - row[i]) == abs(n - i):
                return False
        return True
    
    def dfs(n):
        global ans

        if n == N:
            ans += 1
            return
        
        # N * N의 N개의 퀸을 row에 놓음
        for i in range(N):
            row[n] = i
            # 검사에서 통과하면 dfs함수 다시 실행
            if ck(n):
                dfs(n+1)

    dfs(0)
    print(f'#{T} {ans}')