from itertools import combinations

L, C = map(int,input().split())
c = sorted(input().split())

v = {'a','e','i','o','u'}

for i in combinations(c, L):
    v_count = sum(1 for _ in i if _ in v)

    c_count = L - v_count
    if v_count >= 1 and c_count >= 2:
        print(''.join(i))