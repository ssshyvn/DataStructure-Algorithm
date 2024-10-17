T = int(input())

for i in range(T):
  string = input().split()  # 문자열을 입력받아 공백으로 나눔
  for word in string:
    stack = []  # 빈 스택 생성
    # 단어의 각 문자를 스택에 삽입
    for j in word:
      stack.append(j)
    # 스택에서 문자를 하나씩 꺼내서 출력 (문자열을 뒤집는 효과)
    while stack:
      print(stack.pop(), end='')  # 스택에서 꺼낸 문자 출력
    print(end=' ')  # 단어 사이 공백 출력
  print()  # 한 테스트 케이스 완료 후 줄바꿈
