for T in range(1,int(input())+1):
    N = int(input())
    s = ""
    while len(s) < N:
        a = input().split()
        for i in a:
            s += i

    i = 0
    while True:
        if str(i) not in s:
            break
        i += 1

    print(f'#{T} {i}')