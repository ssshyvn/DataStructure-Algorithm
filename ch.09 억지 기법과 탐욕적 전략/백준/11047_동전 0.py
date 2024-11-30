N, K = map(int, input().split())  # 동전 종류 수 N과 그 가치의 합 K 입력
coin = [int(input()) for _ in range(N)]  # 동전의 가치를 저장할 리스트 생성

count = 0	# 필요한 동전 개수의 최솟값을 저장

for c in reversed(coin):  # 그리디 알고리즘 : 큰 동전부터 사용함
    if K == 0:  # 더 이상 만들 금액이 없으면 종료함
        break
    count += K // c  # 현재 동전으로 사용할 수 있는 최대 개수를 더함
    K %= c  # 해당 동전으로 충당한 금액을 제외하고 남은 금액 계산

print(count)	# 목표 금액 K를 만드는데 필요한 최소 동전 개수 출력
