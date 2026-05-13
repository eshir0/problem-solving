for T in range(1,int(input())+1):
    N = int(input())
    A = list(map(int,input().split()))

    k = 0

    ans = -1

    t = True

    for i in range(N - 1):
        for j in range(i+1,N):
            k = A[i] * A[j]
            k = str(k)

            v = True

            for n in range(len(k) - 1):
                try:
                    if k[n] <= k[n+1]:
                        pass
                    else:
                        v = False
                        break
                except:
                    break
            
            if v:
                ans = max(ans,int(k))

    print(f'#{T} {ans}')