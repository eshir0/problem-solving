# 내가 한 방식 (시간초과 남)
def eval1(a,op,b):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return int(a / b)

for T in range(1,int(input())+1):
    N = int(input())
    Kn = list(map(int,input().split()))
    number = list(map(int,input().split()))

    K = []
    for i in range(len(Kn)):
        if i == 0:
            for j in range(Kn[i]):
                K.append("+")
        elif i == 1:
            for j in range(Kn[i]):
                K.append("-")
        elif i == 2:
            for j in range(Kn[i]):
                K.append("*")
        elif i == 3:
            for j in range(Kn[i]):
                K.append("/")
    
    amax = -1e9
    amin = 1e9
    v = [False] * len(K)
    k = []

    def dfs(n):
        global amax, amin

        if n == len(K):
            
            cost = number[0]
            for i in range(len(k)):
                cost = eval1(cost, k[i], number[i+1])

            amax = max(amax,cost)
            amin = min(amin,cost)
            return
        
        for i in range(len(K)):
            if not v[i]:
                v[i] = True
                k.append(K[i])
                dfs(n+1)
                k.pop()
                v[i] = False

    dfs(0)
    print(f'#{T} {(amax - (amin))}')

# ai가 알려준 방식
for T in range(1,int(input())+1):
    N = int(input())
    Kn = list(map(int,input().split()))
    number = list(map(int,input().split()))

    amax = -1e9
    amin = 1e9

    def dfs(n, cost, add, sub, mul, div):
        global amax, amin

        if n == N:
            amax = max(amax,cost)
            amin = min(amin,cost)
            return
        
        if add > 0:
            dfs(n + 1, cost + number[n], add - 1, sub, mul, div)
        if sub > 0:
            dfs(n + 1, cost - number[n], add, sub - 1, mul, div)
        if mul > 0:
            dfs(n + 1, cost * number[n], add, sub, mul - 1, div)
        if div > 0:
            dfs(n + 1, int(cost / number[n]), add, sub, mul, div - 1)
    
    dfs(1, number[0], Kn[0], Kn[1], Kn[2], Kn[3])
    
    print(f'#{T} {int(amax - (amin))}')