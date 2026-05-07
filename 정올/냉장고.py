N = int(input())
m = []
for _ in range(N):
    a,b = map(int,input().split())
    m.append([b,a])

m = sorted(m)

ans = 1
t = m[0][0]

for i in range(1,N):
    l = m[i][1]
    r = m[i][0]

    if l > t:
        ans += 1
        t = r

print(ans)