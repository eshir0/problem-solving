for T in range(1,11):
    N = int(input())
    m = list(map(int,input().split()))

    ans = 0
    for i in range(2,len(m)-2):
        a = max(m[i-1],m[i-2])
        b = max(m[i+1],m[i+2])
        if a < m[i] and b < m[i]:
            c = max(a,b)
            ans += m[i] - c
            
    print(f'#{T} {ans}')