for _ in range(1,11):
    a = int(input())
    N,M = map(int,input().split())

    c = 0
    c = N**M
    print(f'#{_} {c}')