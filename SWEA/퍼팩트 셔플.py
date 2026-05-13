# 내가 한 방식
for T in range(1,int(input())+1):
    N = int(input())
    M = list(input().split())

    a,b = [],[]
    v = True

    if len(M) % 2 == 0:
        for i in range(len(M)//2):
            a.append(M[i])
        for i in range(len(M)//2,len(M)):
            b.append(M[i])
    else:
        for i in range((len(M)//2)+1):
            a.append(M[i])
        for i in range((len(M)//2)+1,len(M)):
            b.append(M[i])

    ans = []
    for i in range(len(a)):
        try:
            ans.append(a[i])
            ans.append(b[i])
        except:
            pass
        
    print(f'#{T}',*ans)

# ai 추천 방식
for T in range(1,int(input())+1):
    N = int(input())
    M = list(input().split())

    # 바뀐것
    mid = (N + 1) // 2
    a = M[:mid]
    b = M[mid:]

    ans = []
    for i in range(len(a)):
        try:
            ans.append(a[i])
            ans.append(b[i])
        except:
            pass
        
    print(f'#{T}',*ans)