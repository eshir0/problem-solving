from itertools import permutations

def R(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

T = int(input())

for _ in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))

    C = (data[0], data[1])
    home = (data[2], data[3])

    c = []
    for i in range(4, len(data), 2):
        c.append((data[i],data[i+1]))
    
    total = float('inf')

    for i in permutations(c):
        d = 0
        s = C

        for j in i:
            d += R(s,j)
            s = j
        d += R(s,home)

        if d < total:
            total = d

    print(f'#{_} {total}')