from collections import deque
for _ in range(1,11):
    b = int(input())
    a = deque(map(int,input().split()))
    I = False
    while not I:
        for i in range(1,6):
            num = a.popleft() - i
            if num <= 0:
                a.append(0)
                I = True
                break
            a.append(num)
    print(f'#{b}', *a)