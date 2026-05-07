from collections import deque

N = int(input())
K = int(input())

m = [[0]*N for _ in range(N)]

for _ in range(K):
    y,x = map(int,input().split())
    m[y-1][x-1] = 1

L = int(input())
T = {}
for _ in range(L):
    sec,d = input().split()
    T[int(sec)] = d

dy = [0,1,0,-1]
dx = [1,0,-1,0]
D = 0

q = deque([(0,0)])
m[0][0] = 2
time = 0

while True:
    time += 1
    y,x = q[-1]

    ny = y + dy[D]
    nx = x + dx[D]

    if 0<=ny<N and 0<=nx<N and m[ny][nx] != 2:
        if m[ny][nx] ==1:
            m[ny][nx] = 2
            q.append((ny,nx))
        elif m[ny][nx] == 0:
            m[ny][nx] = 2
            q.append((ny,nx))

            ty,tx = q.popleft()
            m[ty][tx] = 0
    else:
        break

    if time in T:
        if T[time] == 'D':
            D = (D+1)%4
        else:
            D = (D-1)%4
print(time)