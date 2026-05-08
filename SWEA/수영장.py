# 가장 적은 비용을 구해야 함.
#
# cost는 순서대로 1일, 1달, 3달, 1년 으로 나뉨
# 1년을 기준으로 가장 적은 비용을 구하면 될것 같음
# 
# 각 달 마다 얼마인지 비교 -> 1일 금액 합 과 1달의 금액 비교
# 1월부터 언제든 3달 이용권을 결제하고 3개월 뒤로 건너뜀
#
# dfs를 활용하면 될것 같음

for T in range(1,int(input())+1):
    cost = list(map(int,input().split()))
    m = list(map(int,input().split()))

    # 최대 값을 1년치 금액으로 미리 잡아둠.
    ans = cost[3]

    def dfs(n,co):
        global ans

        # 현재까지 누적된 요금이 이미 구해둔 최소 요금 이상이면 더 볼 필요 없이 탐색 종료 (가지치기)
        if co >= ans:
            return
        
        # 월이 12개월이 다 지나면 구한 1년 이용 금액을 ans 저장
        if n >= 12:
            ans = co
            return

        # 1일 금액 총 계산
        dfs(n+1,co + (m[n] * cost[0]))
        
        # 1달 금액 총 계산 (전에 계산한 금액 + 계산)
        dfs(n+1,co + cost[1])
        
        # 3달 금액 총 계산 (전에 계산한 금액 + 계산)
        dfs(n+3, co + cost[2])

    dfs(0,0)
    print(f'#{T} {ans}')