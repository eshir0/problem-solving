# 직접 만든 코드

m = [[0] * 300 for i in range(300)]

k = 0

for i in range(1, 300):
    for j in range(1, i+1):
        x = j
        y = i - x + 1
        k += 1
        m[x][y] = k

for T in range(1,int(input())+1):
    N = list(map(int,input().split()))

    v = True

    r,c = 0,0
    y,x = 0,0

    cnt = 0

    for i in range(1,300):
        for j in range(1,300):
            if m[i][j] in N and v:
                y,x = i,j
                v = False
                cnt = 1
            elif m[i][j] in N and not v:
                r,c = i,j
                cnt = 2
    if N[0] == N[1]:
        ny,nx = y+y,x+x
    else:
        ny,nx = r+y,c+x
    print(f'#{T} {m[ny][nx]}')

# ai가 만든 코드

# 1. 2차원 배열과 좌표 저장용 리스트를 한 번에 생성 (시간 초과 방지)
m = [[0] * 300 for _ in range(300)]
pos = {} # (x, y) 튜플을 저장

k = 1
for d in range(1, 300): # d는 대각선의 번호 (좌표의 합 - 1)
    for x in range(1, d + 1):
        y = d - x + 1
        m[x][y] = k
        pos[k] = (x, y) # 숫자 k의 위치가 (x, y)임을 저장
        k += 1

for T in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    
    # 2. O(1)의 속도로 p와 q의 좌표를 즉시 가져옴
    x1, y1 = pos[p]
    x2, y2 = pos[q]
    
    # 3. 새로운 좌표의 위치를 더해서 배열에서 값을 찾음
    nx, ny = x1 + x2, y1 + y2
    print(f'#{T} {m[nx][ny]}')