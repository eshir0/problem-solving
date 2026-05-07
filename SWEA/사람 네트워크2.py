from collections import deque
T = int(input())
for _ in range(1,T+1):
    A = list(map(int,input().split()))
    N = A[0]
    m = []
    for i in range(1,len(A),N):
        m.append(A[i:i + N])

    cc = float('inf')

    for start in range(N):
        q = deque([start])

        dist = [-1] * N
        dist[start] = 0

        while q:
            c = q.popleft()

            for i in range(N):

                if m[c][i] == 1 and dist[i] == -1:
                    dist[i] = dist[c] + 1
                    q.append(i)

        C = sum(dist)
        cc = min(cc,C)
    print(f'#{_} {cc}')