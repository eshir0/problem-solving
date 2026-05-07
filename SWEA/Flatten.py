for _ in range(10):
    M = int(input())
    S = list(map(int,input().split()))

    for i in range(M):
        s = max(S)
        S.remove(s)
        S.append(s - 1)
        
        s = min(S)
        S.remove(s)
        S.append(s + 1)

    print(f'#{_+1} {max(S)-min(S)}')