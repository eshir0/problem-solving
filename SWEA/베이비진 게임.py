for T in range(1,int(input())+1):
    number = list(map(int,input().split()))

    v = True

    p1 = [0] * 10
    p2 = [0] * 10

    ans = 0

    for i in number:
        
        if v:
            p1[i] += 1
            v = False
        elif not v:
            p2[i] += 1
            v = True

        if 3 in p1:
            ans = 1
            break
        elif 3 in p2:
            ans = 2
            break

        for j in range(8):
            if sum(p1[j:j+3]) >= 3 and 0 not in p1[j:j+3]:
                ans = 1
                break
        if ans == 1:
            break

        for j in range(8):
            if sum(p2[j:j+3]) >= 3 and 0 not in p2[j:j+3]:
                ans = 2
                break
        if ans == 2:
            break
    
    print(f'#{T} {ans}')