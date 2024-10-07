# 하노이의 탑
def hanoi_tower(n, fr, tmp, to):    # n: 원판의 수   fr: 시작 막대    tmp: 임시 막대    to: 목표 막대
  if (n==1):                        # 순환 호출을 멈추는 부분. 원판이 하나라면 바로 이동
    print("원판 1: %s --> %s" %(fr, to))
  else:                             # 순환 호출 부분
    hanoi_tower(n-1, fr, to, tmp)             # 단계 1
    print("원판 %d: %s --> %s" %(n, fr, to))  # 단계 2
    hanoi_tower(n-1, tmp, fr, to)             # 단계 3

hanoi_tower(4, 'A', 'B', 'C')
