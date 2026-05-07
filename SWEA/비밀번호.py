for c in range(1,11):
    k , a = input().split()
    s = []
    for i in a:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
    print(f'#{c} ', *s, sep='')