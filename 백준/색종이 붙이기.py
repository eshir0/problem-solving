# 10x10 맵 입력받기
m = [list(map(int,input().split())) for _ in range(10)]

# 인덱스 1~5를 그대로 쓰기 위해 0번 인덱스는 더미(0)로 둡니다.
# 1x1 ~ 5x5 색종이는 각각 5장씩 주어집니다.
paper = [0, 5, 5, 5, 5, 5] 

# 처음에 질문하셨던 float('inf')를 활용하여 최솟값 갱신 준비!
ans = float('inf')

# [도움 함수 1] 해당 y, x 위치에 특정 size의 색종이를 덮을 수 있는지 검사
def can(y, x, size):
    # 맵 밖으로 삐져나가는지 확인
    if y + size > 10 or x + size > 10:
        return False
        
    # 색종이 크기만큼의 공간이 모두 1인지 확인
    for i in range(y, y + size):
        for j in range(x, x + size):
            if m[i][j] != 1:
                return False
    return True

# [도움 함수 2] 색종이를 붙이거나(0) 떼는(1) 동작을 수행
def do(y, x, size, state):
    for i in range(y, y + size):
        for j in range(x, x + size):
            m[i][j] = state

# [메인 로직] DFS 탐색
def dfs(y, x, c):
    global ans
    
    # 1. 종료 조건: 끝 줄(y=10)까지 무사히 다 탐색했다면?
    if y == 10:
        ans = min(ans, c)
        return
        
    # 2. 줄 바꿈: 가로줄(x) 끝까지 갔다면 다음 줄(y+1)의 처음(0)으로 이동
    if x == 10:
        dfs(y + 1, 0, c)
        return
        
    # 3. 가지치기 (핵심 최적화): 이미 구한 최솟값보다 종이를 더 많이 썼다면 즉시 중단
    if c >= ans:
        return

    # 4. 색종이를 붙여야 하는 곳(1)을 만났을 때
    if m[y][x] == 1:
        # 5x5 큰 색종이부터 1x1 작은 색종이까지 순서대로 시도
        for size in range(5, 0, -1):
            if paper[size] > 0 and can(y, x, size):
                
                # [백트래킹 1단계] 붙이기
                do(y, x, size, 0)
                paper[size] -= 1
                
                # [백트래킹 2단계] 다음 칸(x+1)으로 이어서 탐색 진행
                dfs(y, x + 1, c + 1)
                
                # [백트래킹 3단계] 떼기 (원상복구)
                do(y, x, size, 1)
                paper[size] += 1
                
    # 5. 이미 덮여있거나 0인 곳은 바로 통과
    else:
        dfs(y, x + 1, c)

# y=0, x=0 위치부터, 사용한 색종이 0장으로 시작!
dfs(0, 0, 0)

# 만약 맵을 다 덮지 못해서 ans가 갱신되지 않았다면 -1 출력
if ans == float('inf'):
    print(-1)
else:
    print(ans)