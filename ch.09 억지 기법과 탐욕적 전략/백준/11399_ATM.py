N = int(input())  # 사람의 수 입력
P = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 걸리는 시간 

P.sort()	# 탐욕적 기법을 써서 시간을 가장 적게 소모하는 사람부터 처리 -> 시간을 오름차순으로 정렬

total = 0	# 모든 사람의 대기 시간 합
temp = 0	# 각 사람이 인출하는데 걸린 시간의 누적 합

for time in P:
    temp += time  # 현재 사람의 돈 인출 시간을 더함
    total += temp  # 그 사람까지 기다린 시간을 더함

print(total)	# 전체 대기 시간의 합을 출력
