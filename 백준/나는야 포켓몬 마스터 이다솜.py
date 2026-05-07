N,M = map(int,input().split())

m = {}

for i in range(1, N+1):
    name = input()
    
    m[i] = name
    m[name] = i

for i in range(M):
    a = input()
    if a.isdigit():
        print(m[int(a)])
    else:
        print(m[a])