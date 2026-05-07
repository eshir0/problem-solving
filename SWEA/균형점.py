a = int(input())
for c in range(1, a+1):
    N = int(input())
    data = list(map(float,input().split()))

    C = data[:N]
    M = data[N:]

    ans = []

    for i in range(N-1):
        L = C[i]
        R = C[i+1]

        while R-L> 1e-12:
            mid = (L+R) / 2

            l = 0
            r = 0

            for j in range(i+1):
                l += M[j] / ((C[j] - mid) ** 2)

            for j in range(i+1, N):
                r += M[j] / ((mid - C[j]) ** 2)
            
            if l > r:
                L = mid
            else:
                R = mid
        ans.append(f"{mid:.10f}")
    print(f"#{c} {' '.join(ans)}")