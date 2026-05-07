T = int(input())
for _ in range(1,T+1):
    B = list(map(int,input().split()))
    A = list(map(int,input().split()))

    V = B[0]
    E = B[1]

    N = {}
    tree = {}
    for i in range(0,len(A),2):
        j = A[i]
        c = A[i+1]
        N[c] = j

        if j not in tree:
            tree[j] = []
        tree[j].append(c)

    a = []
    c = B[2]
    while c in N:
        a.append(c)
        c = N[c]
        a.append(c)
    
    b = []
    c = B[3]
    while c in N:
        b.append(c)
        c = N[c]
        b.append(c)

    l = 0
    for i in a:
        if i in b:
            l = i
            break

    cnt = 0
    q = [l]
    while q:
        c = q.pop(0)
        cnt += 1

        if c in tree:
            for C in tree[c]:
                q.append(C)

    print(f'#{_} {l} {cnt}')