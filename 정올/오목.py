m = [list(map(int,input().split())) for _ in range(19)]

d = [(0,1), (1,0), (1,1), (-1,1)]

for y in range(19):
    for x in range(19):
        if m[y][x] != 0:
            c = m[y][x]

            for dy, dx in d:
                ny, nx = y + dy, x + dx
                cnt = 1

                while 0 <= ny < 19 and 0 <= nx < 19 and m[ny][nx] == c:
                    cnt += 1
                    ny += dy
                    nx += dx
                if cnt == 5:
                    py, px = y -dy, x - dx

                    if 0 <= py < 19 and 0 <= px < 19 and m[py][px] == c:
                        continue
                    print(c)
                    print(y + 1, x + 1)
                    exit(0)
print(0)