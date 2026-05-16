from collections import deque
for T in range(1,int(input())+1):
    N, M = map(int,input().split())

    v = [False] * 1000001
    
    def bfs(Num,m):
        q = deque()
        q.append((Num,0))
        v[Num] = True
        
        while q:
            now, count = q.popleft()

            if now == m:
                return count
                
            for n in (now + 1, now - 1, now * 2, now - 10):
                if 1 <= n <= 1000000 and not v[n]:
                    v[n] = True
                    q.append((n,count + 1))

    ans = bfs(N,M)
    print(f'#{T} {ans}')