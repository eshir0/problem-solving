N,M = map(int,input().split())
n = list(map(int,input().split()))

m = [i for i in range(1, N+1) if i not in n]


b = []
for i in range(len(n)):
    if n[i] == 0:
        b.append(i)

v = [False] * len(m)
c = 0

def g(arr):
    s = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                s += 1
    return s
    
def s(d):
    global c
    if d == len(b):
        if g(n) == M:
            c += 1        
        return

    for i in range(len(m)):
        if not v[i]:
            v[i] = True
            n[b[d]] = m[i]

            s(d+1)

            n[b[d]] = 0
            v[i] = False


s(0)
print(c)