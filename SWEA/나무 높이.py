for _ in range(1,int(input())+1):
    N = int(input())
    n = list(map(int,input().split()))

    r = max(n)
    a = 0 # 홀수 날짜
    b = 0 # 짝수 날짜

    for i in n:
        d = r - i
        a += d % 2
        b += d // 2

    while b > a + 1:
        a += 2
        b -= 1
    
    if a > b:
        ans = a * 2 - 1
    elif a == b:
        ans = a * 2
    else:
        ans = b * 2
    print(f'#{_} {ans}')