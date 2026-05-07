for T in range(1,int(input())+1):
    N, K = map(int,input().split())
    number = input()

    b = []

    for i in range(0,len(number),N//4):
        b.append(number[i: i + (N//4)])
        
    for j in range(N//4):
        number = number[-1] + number[:-1]
        for i in range(0,len(number),N//4):
            b.append(number[i: i + (N//4)])
    
    a = set(b)
    a = sorted(a, reverse=True)
    
    r = a[K-1]

    print(f'#{T} {int(r,16)}')