N = int(input())
m = [list(map(int,input().split())) for _ in range(N)]

n = []
for i in range(N):
    n.append([m[i][2],m[i][1],m[i][0]])
n = sorted(n)

r = []
ans = 0
e = 0

for end, start, num in n:
    if start >= e:
        ans += 1
        r.append(num)
        e = end
print(ans)
print(*r)