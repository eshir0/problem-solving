for _ in range(1, int(input())+1):
    i, n = input().split()
    a = list(input().split())
    orber = {"ZRO" : 0, "ONE" : 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    w = sorted(a, key=orber.get)
    print(f'#{_}')
    print(*w)