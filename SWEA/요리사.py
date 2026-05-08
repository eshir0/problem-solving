for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    ans = 1e9
    v = [[False] * N for _ in range(N)]

    def dfs(n,cnt):
        global ans

        if cnt == N//2:
            
            # 식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 시작
            a,b = [],[]
            for i in range(N):
                if v[i]:
                    a.append(i)
                else:
                    b.append(i)

            # 나눈 식재료들을 요리로 만들어 전부 합침
            A,B = 0,0
            
            for i in range(len(a)):
                for j in range(i+1, len(a)):
                    A += m[a[i]][a[j]] + m[a[j]][a[i]]
            
            for i in range(len(b)):
                for j in range(i+1, len(b)):
                    B += m[b[i]][b[j]] + m[b[j]][b[i]]

            # 합친 요리의 맛 점수들을 뺌 -> 맛의 차이 S를 얻음
            S = abs(A-B)

            # 맛의 차이가 제일 낮은게 나올때까지 함.
            if S < ans:
                ans = S
            
            return

        # index 범위를 벗어나지 않게 하기 위한 것
        if n == N:
            return

        # 각 재료 N/2 만큼 얻을수 있게 하는 모든 경우의 수
        v[n] = True
        dfs(n+1,cnt+1)
        v[n] = False
        dfs(n+1,cnt)

    dfs(0,0)
    print(f'#{T} {ans}')