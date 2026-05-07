# 1
import sys

N,M = map(int, sys.stdin.readline().split())
v = [False] * (N + 1)
a = []

def s(d):
    if d == M:
        print(*a)
        return
    
    for i in range(1, N + 1):
        if not v[i]:
            v[i] = True
            a.append(i)
            s(d + 1)
            # 상태 복구(Backtrack)
            a.pop()
            v[i] = False
s(0)

# 2
import sys
N, M = map(int, sys.stdin.readline().split())
v = [False] * (N+1)
a = []

def s(d, st):
    if d == M:
        print(*a)
        return
    
    for i in range(st, N+1):
        if not v[i]:
            v[i] = True
            a.append(i)
            s(d+1, i+1)
            
            a.pop()
            v[i] = False
s(0,1)

# 3
import sys
N, M = map(int,sys.stdin.readline().split())
a = []

def s(d):
    if d==M:
        print(*a)
        return
    
    for i in range(1, N+1):
        a.append(i)
        s(d+1)
        a.pop()
s(0)

# 4
import sys
N, M = map(int,sys.stdin.readline().split())
a = []

def s(d,st):
    if d==M:
        a.sort()
        print(*a)
        return
    
    for i in range(st, N+1):
        a.append(i)
        s(d+1, i)
        a.pop()
s(0,1)

# 5
import sys
N,M = map(int,sys.stdin.readline().split())
n = list(map(int,sys.stdin.readline().split()))
n.sort()
v = [False] * (N+1)
a = []

def s(d):
    if d == M:
        print(*a)
        return
    
    for i in range(len(n)):
        if not v[i]:
            v[i] = True
            a.append(n[i])
            s(d+1)
            a.pop()
            v[i] = False
s(0)

# 6
import sys
N,M = map(int,sys.stdin.readline().split())
n = list(map(int,sys.stdin.readline().split()))
n.sort()
v = [False] * N
a = []

def s(d, st):
    if d == M:
        print(*a)
        return
    
    for i in range(st , N):
        if not v[i]:
            v[i] = True
            a.append(n[i])
            s(d+1,i)
            a.pop()
            v[i] = False
s(0,0)

# 7
import sys
N,M = map(int,sys.stdin.readline().split())
n = list(map(int,sys.stdin.readline().split()))
n.sort()
a = []

def s(d):
    if d == M:
        print(*a)
        return
    
    for i in range(N):
        a.append(n[i])
        s(d+1)
        a.pop()
s(0)

# 8
import sys
N,M = map(int,sys.stdin.readline().split())
n = list(map(int,sys.stdin.readline().split()))
n.sort()
a = []

def s(d, st):
    if d == M:
        print(*a)
        return
    
    for i in range(st , N):
            a.append(n[i])
            s(d+1,i)
            a.pop()
s(0,0)

# 9
N,M = map(int,input().split())
n = sorted(list(map(int,input().split())))
v = [False] * N
a = []
def s(d):
    if d == M:
        print(*a)
        return
    b = 0
    for i in range(N):
        if not v[i] and n[i] != b:
            v[i] = True
            a.append(n[i])
            b = n[i]
            s(d+1)
            a.pop()
            v[i] = False
s(0)

# 10
N,M = map(int,input().split())
n = sorted(list(map(int,input().split())))
v = [False] * N
a = []
def s(d,st):
    if d == M:
        print(*a)
        return
    b = 0
    for i in range(st,N):
        if not v[i] and n[i] != b:
            v[i] = True
            a.append(n[i])
            b = n[i]
            s(d+1, i)
            a.pop()
            v[i] = False
s(0,0)

# 11
N,M = map(int,input().split())
n =list(map(int,input().split()))
n = list(set(n))
if n != N:
    N = len(n)
n.sort()
a = []

def s(d):
    if d == M:
        print(*a)
        return
    
    for i in range(N):
        a.append(n[i])
        s(d+1)
        a.pop()
s(0)

# 12
N,M = map(int,input().split())
n =list(map(int,input().split()))
n = list(set(n))
if n != N:
    N = len(n)
n.sort()
a = []

def s(d,st):
    if d == M:
        print(*a)
        return
    
    for i in range(st,N):
        a.append(n[i])
        s(d+1,i)
        a.pop()
s(0,0)