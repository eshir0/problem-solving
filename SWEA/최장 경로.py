for T in range(1,int(input())+1):
    N,M = map(int,input().split())
    
    # 간선 경로 받기
    m = []
    for i in range(M):
        a,b = map(int,input().split())
        m.append([a,b])

    # 편하게 하기 위해 간선 경로를 딕셔너리로 만듬
    q = {}
    for x,y in m:
        if x not in q:
            q[x] = []
        if y not in q:
            q[y] = []
        
        q[x].append(y)
        q[y].append(x)

    ans = 0
    v = [False] * (N+1)
    
    def dfs(n,cnt):
        global ans

        # 원래 최장 경로보다 높으면 값 갱신
        if cnt > ans:
            ans = cnt
        
        # 출발점에서 최장 경로를 탐색하는 코드
        if n in q:
            for node in q[n]:
                if not v[node]:
                    v[node] = True
                    dfs(node, cnt + 1)
                    v[node] = False

    # 모든 노드의 출발점에서 최장 경로 계산
    for i in range(1,N+1):
        v[i] = True
        dfs(i,1)
        v[i] = False

    print(f'#{T} {ans}')