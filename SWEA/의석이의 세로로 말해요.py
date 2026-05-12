for T in range(1,int(input())+1):
    m = [list(input()) for i in range(5)]

    max_ = 0
    for i in range(len(m)):
        max_ = max(max_,len(m[i]))
    
    mp = [[0] * max_ for i in range(5)]

    for i in range(5):
        for j in range(len(m[i])):
            mp[i][j] = m[i][j]

    ans = ""

    for i in range(max_):
        for j in range(5):
            if mp[j][i] != 0:
                ans += mp[j][i]
    
    print(f'#{T} {ans}')