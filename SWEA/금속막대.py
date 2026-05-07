T = int(input())
for _ in range(1,T+1):
    n = int(input())
    ns = list(map(int,input().split()))
    N = []
    for i in range(0,len(ns),2):
        N.append((ns[i],ns[i+1]))
    N.sort()
    b = []
    for i in range(len(N)):
        for j in range(len(N)):
            if N[i][1] == N[j][0]:
                b.append(N[j])

    start = 0
    for i in N:
        if i not in b:
            start = i
            break
    ans = [start]
    for i in range(len(b)):
        for j in range(len(b)):
            if ans[i][1] == b[j][0]:
                ans.append(b[j])
    
    print(f'#{_} ', end='')
    for i in ans:
        print(*i, end=' ')
    print()