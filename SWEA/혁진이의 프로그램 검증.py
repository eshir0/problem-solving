for _ in range(1,int(input())+1):
    R,C = map(int,input().split())
    m = [list(input()) for i in range(R)]

    dy = [0,0,-1,1]
    dx = [1,-1,0,0]

    q = [(0,0,0,0)]
    v = set()
    v.add((0,0,0,0))

    ans = "NO"

    while q:
        y,x,n,d = q.pop(0)

        c = m[y][x]

        if c == ">": d = 0
        elif c == "<": d = 1
        elif c == "^": d = 2
        elif c == "v": d = 3
        elif c == "_": d = 0 if n == 0 else 1
        elif c == "|": d = 3 if n == 0 else 2
        elif c == "+": n = (n + 1) % 16
        elif c == "-": n = (n - 1) % 16
        elif c.isdigit(): n = int(c)
        elif c == "@":
            ans = "YES"
            break

        if c == "?":
            for i in range(4):
                ny = (y + dy[i]) % R
                nx = (x + dx[i]) % C

                if (ny,nx,n,i) not in v:
                    v.add((ny,nx,n,i))
                    q.append((ny,nx,n,i))
        else:
            ny = (y + dy[d]) % R
            nx = (x + dx[d]) % C

            if (ny,nx,n,d) not in v:
                v.add((ny,nx,n,d))
                q.append((ny,nx,n,d))
    print(f'#{_} {ans}')