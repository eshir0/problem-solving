# 찾아보면서 만든 코드
from collections import deque
for T in range(1,int(input())+1):
    N, S = input().split()
    N = int(N)
    m = [list(map(int,input().split())) for i in range(N)]
    
    def tran(board):
        return [list(row) for row in zip(*board)]

    def move_l(row):
        q = deque([i for i in row if i != 0])
        new_row = []

        while q:
            a = q.popleft()
            if q and a == q[0]:
                new_row.append(a * 2)
                q.popleft()
            else:
                new_row.append(a)
            
        return new_row + [0] * (len(row) - len(new_row))

    def move(board,s):
        new_board = []
        if s == "left":
            for row in board: new_board.append(move_l(row))
        elif s == 'right':
            for row in board: new_board.append(move_l(row[::-1])[::-1])
        elif s == "up":
            board = tran(board)
            for row in board: new_board.append(move_l(row))
            new_board = tran(new_board)
        elif s == "down":
            board = tran(board)
            for row in board: new_board.append(move_l(row[::-1])[::-1])
            new_board = tran(new_board)
        return new_board
    
    m = move(m,S)
    print(f'#{T}')
    for i in m:
        print(*i)

# ai가 압축한 버전의 코드
from collections import deque
for T in range(1,int(input())+1):
    N, S = input().split()
    N = int(N)
    m = [list(map(int,input().split())) for i in range(N)]
    
    def tran(board):
        return [list(row) for row in zip(*board)]

    def move_l(row):
        q = deque([i for i in row if i != 0])
        new_row = []

        while q:
            a = q.popleft()
            if q and a == q[0]:
                new_row.append(a * 2)
                q.popleft()
            else:
                new_row.append(a)
            
        return new_row + [0] * (len(row) - len(new_row))

    def move(board, s):
        if s in ("up", "down"):
            board = [list(row) for row in zip(*board)]
            
        new_board = []
        for row in board:
            if s in ("right", "down"):
                new_board.append(move_l(row[::-1])[::-1])
            else:
                new_board.append(move_l(row))
                
        if s in ("up", "down"):
            new_board = [list(row) for row in zip(*new_board)]
            
        return new_board
        
    m = move(m,S)
    print(f'#{T}')
    for i in m:
        print(*i)
