T = int(input())
for _ in range(1,T+1):
    k = int(input())
    a = input()
    b = []
    for i in range(len(a)):
        b.append(a[i:])
    c = list(sorted(b))
    print(f'#{_} {c[k-1]}')