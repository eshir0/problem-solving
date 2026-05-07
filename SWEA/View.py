T = int(input())

for _ in range(T):
    N = int(input())
    h = list(map(int,input().split()))
    v = 0
    for i in range(2,N-2):
        n = max(h[i-2],h[i-1],h[i+1],h[i+2])
        if h[i] > n:
            v += (h[i] - n)
    print(f"#{_+1} {v}")