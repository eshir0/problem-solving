T = int(input())
for _ in range(1,T+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    ans = []

    for i in range(N):
        for j in range(N):
            if m[i][j] != 0:
                r,c = 0,0

                while j + c < N and m[i][j+c] != 0:
                    c += 1
                while i + r < N and m[i+r][j] != 0:
                    r += 1
                
                for y in range(i, i+r):
                    for x in range(j, j+c):
                        m[y][x] = 0
                ans.append((r * c, r, c))

    ans.sort()
    print(f"#{_} {len(ans)}", end="")
    for s, r, c in ans:
        print(f" {r} {c}", end="")
    print()