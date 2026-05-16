from collections import deque
for T in range(1,int(input())+1):
    V, E = map(int,input().split())
   
    node = [[] for _ in range(V + 1)]

    for _ in range(E):
        u,v = map(int,input().split())
        node[u].append(v)
        node[v].append(u)

    S,G = map(int,input().split())

    v = [False] * (V + 1)

    def bfs(start, goal):
        q = deque()

        q.append((start, 0))
        v[start] = True

        while q:
            now, dist = q.popleft()

            if now == goal:
                return dist
            
            for next in node[now]:

                if not v[next]:
                    v[next] = True
                    q.append((next,dist+1))
                    pass
        
        return 0
    
    ans = bfs(S,G)
    print(f'#{T} {ans}')