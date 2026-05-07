from collections import deque
for _ in range(1,11):
    V,E = map(int,input().split())
    N = list(map(int,input().split()))

    n = []
    b = [0] * ( V + 1 )
    for i in range(0,len(N),2):
        n.append((N[i],N[i+1]))
        b[N[i+1]] += 1

    q = deque()
    for i in range(1, V + 1):
        if b[i] == 0:
            q.append(i)

    ans = []

    while q:
        cnt = q.popleft()
        ans.append(cnt)

        for u, v in n:
            if u == cnt:
                b[v] -= 1
                if b[v] == 0:
                    q.append(v)
    print(f'#{_}', end=' ')
    print(*ans)