# 반복 구조의 팩토리얼 함수
def factorial_iter(n):
  result=1
  for i in range(2, n+1):  # k: 2, 3, ..., n
    result*=i              # result에 k를 곱함
  return result

factorial_iter(5)

# 순환 구조의 팩토리얼 함수
def factorial(n):
  if n==1:    # 순환 호출을 멈추는 부분. n이 1이면 답을 알고 있음.
    return 1
  else:       # 자신을 순환적으로 호출하는 부분. 문제의 크기는 작아져야 함.
    return n*factorial(n-1)

factorial(5)
