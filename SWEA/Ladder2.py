for _ in range(10):
    a = int(input())
    m = [list(map(int,input().split())) for i in range(100)]

    b = float('inf')
    ans = -1

    for i in range(100):
        if m[0][i] == 1:
            y,x = 0 , i
            dist = 0

            while y < 99:

                if x > 0 and m[y][x - 1] == 1:
                    while x > 0 and m[y][x - 1] == 1:
                        x -= 1
                        dist += 1
                elif x < 99 and m[y][x + 1] == 1:
                    while x < 99 and m[y][x + 1] == 1:
                        x += 1
                        dist += 1
                y += 1
                dist += 1

            if dist < b:
                b = dist
                ans = i
            elif dist == b:
                ans = max(ans, i)
    print(f'#{a} {ans}')