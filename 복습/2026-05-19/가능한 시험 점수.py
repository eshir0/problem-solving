for T in range(1,int(input())+1):
    N = int(input())
    m = list(map(int,input().split()))

    ans = {0}

    for i in m:
        for j in list(ans):
            ans.add(j+i)

    print(f'#{T} {len(ans)}')