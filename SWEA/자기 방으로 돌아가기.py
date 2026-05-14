for T in range(1,int(input())+1):
    N = int(input())

    h = [0] * 201

    for _ in range(N):
        start, end = map(int,input().split())

        if start > end:
            start, end = end, start
        
        s = (start + 1) // 2
        e = (end + 1) // 2

        for j in range(s, e + 1):
            h[j] += 1

    print(f'#{T} {max(h)}')