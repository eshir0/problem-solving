T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    m = [input() for i in range(N)]
    
    hex = {
        '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
        '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
        '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
        'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111'
    }

    r = {
        (1, 1, 2): 0, (1, 2, 2): 1, (2, 2, 1): 2, (1, 1, 4): 3,
        (2, 3, 1): 4, (1, 3, 2): 5, (4, 1, 1): 6, (2, 1, 3): 7,
        (3, 1, 2): 8, (2, 1, 1): 9
    }

    ans = 0
    v = set()

    for i in range(N):
        line = ""
        for c in m[i]:
            line += hex[c]
                
        j = len(line) - 1
        code = []

        while j >= 0:
            if line[j] == '1':
                c1 = c2 = c3 = 0

                while j >= 0 and line[j] == '1':
                    c1 += 1
                    j -= 1
                while j >= 0 and line[j] == '0':
                    c2 += 1
                    j -= 1
                while j >= 0 and line[j] == '1':
                    c3 += 1
                    j -= 1
                
                k = min(c1, c2, c3)

                r1, r2, r3 = c1//k, c2//k, c3//k

                d = r.get((r1, r2, r3))
                if d is not None:
                    code.append(d)
                
                j -= (7*k - (c1+c2+c3))

                if len(code) == 8:
                    code.reverse()
                    t = tuple(code)

                    if t not in v:
                        v.add(t)
                        
                        ck = ((code[0] + code[2] + code[4] + code[6]) * 3) + code[1] + code[3] + code[5] + code[7]
                        
                        if ck % 10 == 0:
                            ans += sum(code)
                    code = []
            else:
                j -= 1
                
    print(f'#{_} {ans}')