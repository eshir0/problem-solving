N = list(map(int,input().split()))
n = [[] for _ in range(N[0]+1)]
for _ in range(N[1]):
    a, b = map(int,input().split())
    n[a].append(b)
    n[b].append(a)

for i in range(1, N[0] + 1):
    n[i].sort()

v = [False] * (N[0] +1)

#dfs
def dfs(D):
    v[D] = True
    print(D, end=' ')
    for i in n[D]:
        if not v[i]:
            dfs(i)

from collections import deque

#bfs
def bfs(B):
    V = [False] * (N[0]+1)

    q = deque([B])
    V[B] = True

    while q:
        c = q.popleft()
        print(c, end=' ')

        for i in n[c]:
            if not V[i]:
                V[i] = True
                q.append(i)
    print()
dfs(N[2])
print()
bfs(N[2])