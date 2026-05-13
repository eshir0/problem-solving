for T in range(1,int(input())+1):
    N = int(input())

    ck = ['0','1','2','3','4','5','6','7','8','9']

    k = 1
    b = 0

    while True:
        b = N * k
        b = str(b)

        for i in range(len(b)):
            if b[i] in ck:
                ck.remove(b[i])

        if not ck:
            break

        k += 1

    print(f'#{T} {b}')