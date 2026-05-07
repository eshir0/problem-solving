a = int(input())
b = int(input())
n = [[] for _ in range(a+1)]

for i in range(b):
    x, y = map(int,input().split())
    n[x].append(y)
    n[y].append(x)

# DFS방식
v_dfs = [False] * (a + 1)
c = 0
def dfs(d):
    global c
    v_dfs[d] = True
    for i in n[d]:
        if not v_dfs[i]:
            c +=1
            dfs(i)
dfs(1)
print(c)

# BFS방식
from collections import deque

v_bfs = [False] * (a+1)
c = 0

def bfs(b):
    global c
    
    q = deque([b])
    v_bfs[b] = True

    while q:
        node = q.popleft()
        for i in n[node]:
            if not v_bfs[i]:
                v_bfs[i] = True
                q.append(i)
                c += 1
bfs(1)
print(c)