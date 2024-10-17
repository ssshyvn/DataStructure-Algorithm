stack=[]  # 빈 스택 생성
N=int(input())

for i in range(N):
  order=input().split() # 문자열을 입력받아 공백으로 나눔

  if order[0]=='push':
    stack.append(order[1])

  elif order[0]=='pop':
    if stack:
      print(stack.pop())
    else:
      print(-1)

  elif order[0]=='size':
    print(len(stack))

  elif order[0]=='empty':
    if stack:
      print(0)
    else:
      print(1)

  elif order[0]=='top':
    if stack:
      print(stack[len(stack)-1])
    else:
      print(-1)
