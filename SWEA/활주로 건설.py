for T in range(1,int(input())+1):
    N, X = map(int,input().split())
    M = [list(map(int,input().split())) for i in range(N)]

    ans = 0

    def ck(line):
        # 경사로가 설치된 곳을 표시할 배열
        used = [False] * N

        for i in range(N - 1):
            
            if line[i] == line[i+1]:
                continue

            # 높이 차이가 1보다 크면 경사로 설치 불가
            if abs(line[i] - line[i+1]) > 1:
                return False
            
            # 올라가는 경우 : 왼쪽으로 x칸 검사
            if line[i] < line[i+1]:
                for j in range(X):

                    # 범위를 벗어나거나, 높이가 다르거나, 이미 경사로가 있다면 실패
                    if i - j < 0 or line[i] != line[i - j] or used[i - j]:
                        return False
                    
                    #경사로 설치
                    used[i - j] = True
            
            # 내려가는 경우 : 오른쪽으로 x칸 검사
            elif line[i] > line[i+1]:
                for j in range(X):
                    
                    # 범위를 벗어나거나, 높이가 다르거나, 이미 경사로가 있다면 실패
                    if i + 1 + j >= N or line[i + 1] != line[i + 1 + j] or used[i + 1 + j]:
                        return False
                    
                    # 경사로 설치
                    used[i + 1 + j] = True

        return True

    for i in range(N):
        if ck(M[i]):
            ans += 1
    
    M = [i for i in zip(*M)]

    for i in range(N):
        if ck(M[i]):
            ans += 1

    print(f'#{T} {ans}')