for T in range(1,int(input())+1):
    N = int(input())
    number = list(map(int,input().split()))

    max_ = 0
    ans = 0

    for i in range(len(number)-1, -1, -1):
        if number[i] > max_:
            max_ = number[i]

        else:
            ans += max_ - number[i]

    print(f'#{T} {ans}')