for _ in range(1,11):
    a = int(input())
    b = list(map(int,input().split()))
    c = int(input())

    L = input().split()
    i = 0

    while i < len(L):
        if L[i] == 'I':
            x = int(L[i+1])
            y = int(L[i+2])

            s = list(map(int,L[i+3 : i+3+y]))

            b[x:x] = s
            i += 3 + y
        elif L[i] == 'D':
            x = int(L[i+1])
            y = int(L[i+2])

            del b[x:x+y]
            i += 3
        elif L[i] == 'A':
            y = int(L[i+1])
            s = list(map(int, L[i+2 : i+2+y]))

            b.extend(s)

            i += 2 + y
            
    print(f'#{_}', *b[:10])