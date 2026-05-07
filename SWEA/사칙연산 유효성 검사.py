def f(l):
    for i in l:
        if i[1] in '+-*/':
            if len(i) != 4: 
                return 0
        elif len(i) != 2: 
            return 0
    return 1

for t in range(1, 11):
    n = int(input())
    l = [input().split() for _ in range(n)]
    print(f"#{t} {f(l)}")