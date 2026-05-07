from collections import Counter
for _ in range(1,11):
    a = int(input())
    n = list(map(int,input().split()))

    c = Counter(n)
    c = max(c,key=c.get)

    print(f'#{_} {c}')