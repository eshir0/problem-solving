for _ in range(10):
    a = int(input())
    L = input()
    p = {')':'(', '}':'{',']':'[','>':'<'}
    s = []

    c = 1

    for i in L:
        if i in p.values():
            s.append(i)
        elif i in p.keys():
            if not s or s.pop() != p[i]:
                c = 0
                break
    if c == 0:
        print(f'#{_+1} {0}')
    else:
        print(f'#{_+1} {1}')