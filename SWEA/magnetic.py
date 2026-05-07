for _ in range(1,11):
    N = int(input())
    m = [list(map(int,input().split())) for I in range(100)]

    row = list(map(list, zip(*m)))
    total = 0

    for r in row:
        flag = False

        for i in r:
            if i ==1:
                flag = True
            elif i == 2:
                if flag:
                    total += 1
                    flag = False
    print(f"#{_} {total}")