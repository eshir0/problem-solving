# 내가 만든 코드
for T in range(1,int(input())+1):
    A,B = input().split()
    A = list(A)
    B = list(B)

    cnt = 0
    i = 0

    while i <= len(A) - len(B):
        if A[i:i+len(B)] == B:
            cnt += 1
            del A[i:i+len(B)]
        else:
            i += 1

    print(f'#{T} {len(A)+cnt}')

# ai 힌트 제공
for T in range(1,int(input())+1):
    A,B = input().split()

    a = A.replace(B,"")
    b = A.count(B)

    print(f'#{T} {len(a)+b}')