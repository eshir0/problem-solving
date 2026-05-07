T = int(input())
for _ in range(1,T+1):
    k = int(input())
    a = input()
    b = []
    for i in range(len(a)):
        b.append(a[i])
        for j in range(len(a)):
            b.append(a[i:j+1])
            b.append(a[j+1::])
    d = list(sorted(set(b)))
    c = [i for i in d if i]
    print(f'#{_} {c[k-1]}')