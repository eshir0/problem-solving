for T in range(1,int(input())+1):
    N = int(input())

    v = [0] * 5001

    for i in range(N):
        A,B = map(int,input().split())
        for j in range(A, B + 1):
            v[j] += 1

    ans = []
    P = int(input())
    for i in range(P):
        C = int(input())
        ans.append(v[C])

    print(f'#{T}',*ans)