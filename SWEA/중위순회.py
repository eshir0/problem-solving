# 중위 순회(In-order)를 수행하는 재귀 함수
def in_order(node):
    # 기저 조건(Base case): 노드 번호가 전체 노드 수(N)보다 커지면 유효하지 않으므로 종료
    if node <= N:
        # 1. 왼쪽 자식 노드로 이동 (현재 노드 번호 * 2)
        in_order(node * 2)
        
        # 2. 현재 노드의 값(알파벳) 출력
        # end=''를 사용하여 줄바꿈 없이 이어서 출력되도록 함
        print(tree[node], end='')
        
        # 3. 오른쪽 자식 노드로 이동 (현재 노드 번호 * 2 + 1)
        in_order(node * 2 + 1)

# 문제에서 10개의 테스트 케이스가 주어진다고 명시함
for tc in range(1, 11):
    N = int(input()) # 트리를 구성하는 총 정점의 수
    
    # 1번 인덱스부터 직관적으로 사용하기 위해 크기가 N + 1인 배열 생성
    # 초기값은 빈 문자열로 설정
    tree = [''] * (N + 1)
    
    # N개의 줄에 걸쳐 주어지는 정점 정보 입력받기
    for _ in range(N):
        data = input().split()
        
        # 입력 데이터의 첫 번째는 노드 번호, 두 번째는 해당 노드의 알파벳
        node_num = int(data[0])
        alphabet = data[1]
        
        # 배열의 해당 노드 번호 인덱스에 알파벳을 저장
        # (자식 노드의 번호는 배열 인덱스 연산으로 알 수 있으므로 저장할 필요 없음)
        tree[node_num] = alphabet
        
    # 결과 출력 양식에 맞게 테스트 케이스 번호 먼저 출력
    print(f"#{tc} ", end='')
    
    # 항상 루트 노드인 1번 노드부터 순회 시작
    in_order(1)
    
    # 하나의 테스트 케이스 단어가 완성되면 줄바꿈
    print()

# 짧게
def f(i):
    if i <= n:
        f(i*2)
        print(t[i], end='')
        f(i*2+1)

for c in range(1, 11):
    n = int(input())
    t = [''] * (n + 1)
    for _ in range(n):
        d = input().split()
        t[int(d[0])] = d[1]
    print(f"#{c} ", end='')
    f(1)
    print()