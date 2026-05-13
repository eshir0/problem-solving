for T in range(1,int(input())+1):
    N = int(input())

    ans = [[] for i in range(N)]

    for i in range(N):
        if i == 0:
            for j in range(i+1):
                ans[i].append(1)
        else:
            for j in range(i+1):
                if j == i:
                    ans[i].append(1)
                elif j == 0:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j]+ans[i-1][j-1]) 

    print(f'#{T}')
    for i in range(N):
        print(*ans[i],end='\n')