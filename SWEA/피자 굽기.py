from collections import deque
for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    cheese = list(map(int,input().split()))

    oven = deque()
    wait = deque()

    for i in range(M):
        if i < N:
            oven.append([i + 1, cheese[i]])
        else:
            wait.append([i + 1, cheese[i]])

    while len(oven) > 1:
        l = oven.popleft()
        n,k = l
        k = k // 2
        if k == 0:
            if wait:
                l = wait.popleft()
                oven.append(l)
        else:
            oven.append([n,k])
            
    print(f'#{T} {oven[0][0]}')