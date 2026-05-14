# 각 S극이 화살표 방향일 때 점수 : 1, 2, 4, 8
# 회전이 끝났을때 각 화설표 부분에 총 점수 계산
# N극이 0 , S극이 1
# K는 회전 수
# 시계방향은 1, 반시계방향은 -1

# 시계방향과 반시계방향을 하기위해 deque를 씀
from collections import deque
for T in range(1,int(input())+1):
    K = int(input())

    # 4개의 자석
    M = [deque(map(int,input().split())) for i in range(4)]

    for _ in range(K):
        n,d = map(int,input().split())
        # 0으로 맞추기 위함.
        idx = n - 1

        # 현재 턴에 각 자석이 어느 방향으로 돌지 기록할 배열 (0 제외)
        v = [0] * 4
        v[idx] = d

        # 기준 자석에서 왼쪽 자석들 검사
        for i in range(idx - 1, -1, -1):
            # 오른쪽 자석의 6번 극 != 왼쪽 자석의 2번 극이면 연쇄 회전
            if M[i][2] != M[i+1][6]:
                # 반대 방향으로 회전 기록
                v[i] = -v[i+1]
            else:
                break
        
        # 기준 자석에서 오른쪽 자석들 검사
        for i in range(idx + 1, 4):
            # 왼쪽 자석의 2번 극 != 오른쪽 자석의 6번 극이면 연왜 회전
            if M[i-1][2] != M[i][6]:
                # 정 방향으로 회전 기록
                v[i] = -v[i-1]
            else:
                break

        # 회전 기록이 마치면 deque의 rotate()로 한꺼번에 돌림
        for i in range(4):
            if v[i] != 0:
                # 1이면 시계, -1이면 반시계로 알아서 밀림
                M[i].rotate(v[i])

    # 최종 점수 계산
    ans = (M[0][0] * 1) + (M[1][0] * 2) + (M[2][0] * 4) + (M[3][0] * 8)
    
    print(f'#{T} {ans}')