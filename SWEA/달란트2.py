T = int(input())
for _ in range(1,T+1):
    N, P = map(int,input().split())
    q = N // P
    r = N % P

    n = ((q+1) ** r) * (q ** (P-r))

    print(f'#{_} {n}')