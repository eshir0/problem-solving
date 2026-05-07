for _ in range(1,11):
    a = int(input())
    b = list(map(int,input().split()))
    c = int(input())
    l = input().split('I')

    for cnd in l:
        if len(cnd) == 0: continue

        L = list(map(int, cnd.split()))
        
        x = L[0]
        y = L[1]
        s = L[2:]

        b[x:x] = s
    print(f'#{_}', *b[:10])