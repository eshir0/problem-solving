from itertools import combinations

while True:
    L = list(map(int,input().split()))
    if L[0] == 0:
        break

    for c in combinations(L[1:], 6):
        print(*c)
    print()