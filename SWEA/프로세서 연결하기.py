# 전체 테스트 케이스의 개수를 입력받음
a = int(input())

# a개의 테스트 케이스만큼 반복
for p in range(1, a + 1):
    # 맵의 크기 N 입력
    N = int(input())
    # N x N 크기의 2차원 맵 정보 입력
    m = [list(map(int, input().split())) for i in range(N)]

    c = []
    # 맵 전체를 탐색하며 코어(1)의 위치를 찾음
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                # 맵의 가장자리(벽)에 이미 붙어있는 코어는 이미 연결된 상태이므로 제외하고,
                # 내부(안쪽)에 있는 코어의 좌표만 c 리스트에 추가
                if i != 0 and i != N - 1 and j != 0 and j != N - 1:
                    c.append((i, j))

    # 현재 테스트 케이스에서 사용할 전역 변수 초기화
    maxc = 0             # 가장 많이 연결한 코어의 개수
    minl = float('inf')  # 그때의 최소 전선 길이 (초깃값은 무한대)

    # 4방향 탐색을 위한 델타값 (상, 하, 좌, 우)
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    # DFS 백트래킹 함수 정의
    # n: 현재 탐색 중인 코어의 인덱스, cnt: 현재까지 연결된 코어 수, line: 현재까지 깐 전선의 총 길이
    def dfs(n, cnt, line):
        global maxc, minl
        
        # [종료 조건] 리스트에 담긴 모든 내부 코어를 다 확인했을 때
        if n == len(c):
            # 1. 기존 기록보다 더 많은 코어를 연결했다면 무조건 정답 갱신
            if cnt > maxc:
                maxc = cnt
                minl = line
            # 2. 코어 연결 개수가 기존 최대치와 같다면, 전선 길이가 더 짧을 때만 갱신
            elif cnt == maxc:
                if line < minl:
                    minl = line
            return
        
        # 이번에 탐색할 코어의 x(행), y(열) 좌표
        x, y = c[n]

        # 4가지 방향(상, 하, 좌, 우)으로 전선 연결 시도
        for i in range(4):
            count = 0        # 이번 방향으로 깔게 될 전선 길이
            can = True       # 이 방향으로 무사히 벽까지 갈 수 있는지 확인하는 스위치
            
            # 현재 코어 위치에서 출발
            nx, ny = x, y 
            
            # 1단계: 벽에 닿을 때까지 가상으로 전진해보기
            while True:
                ny += dy[i]
                nx += dx[i]

                # 맵 밖으로 나갔다 = 무사히 벽에 닿았다 (탐색 성공)
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    break
                
                # 가는 길에 다른 코어(1)나 이미 깔린 전선(2)을 만났다 (탐색 실패)
                if m[nx][ny] != 0:
                    can = False
                    break
                    
                # 빈칸이면 전선 길이를 1 늘리고 계속 직진
                count += 1
                
            # 2단계: 무사히 벽에 도달했다면 (can == True)
            if can:
                # 실제로 맵에 전선 깔기 (해당 칸들을 2로 변경)
                fill_x, fill_y = x, y
                for _ in range(count):
                    fill_y += dy[i]
                    fill_x += dx[i]
                    m[fill_x][fill_y] = 2

                # 전선을 깔았으니, 코어 개수와 전선 길이를 늘려서 다음 코어(n+1) 탐색으로 넘어감
                dfs(n + 1, cnt + 1, line + count)

                # 3단계: 다음 코어 탐색을 마치고 돌아왔으면, 다른 방향 탐색을 위해 깔았던 전선 다시 치우기 (백트래킹)
                fill_x, fill_y = x, y
                for _ in range(count):
                    fill_y += dy[i]
                    fill_x += dx[i]
                    m[fill_x][fill_y] = 0  # 0으로 원상 복구

        # 4가지 방향을 다 확인한 후, 이 코어를 아예 연결하지 않고 '포기'한 채로 다음 코어로 넘어가는 경우도 탐색
        dfs(n + 1, cnt, line)

    # 0번째 코어부터 탐색 시작 (연결 코어 0개, 전선 길이 0)
    dfs(0, 0, 0)
    
    # 해당 테스트 케이스 번호와 찾아낸 최소 전선 길이를 출력 형식에 맞춰 출력
    print(f'#{p} {minl}')