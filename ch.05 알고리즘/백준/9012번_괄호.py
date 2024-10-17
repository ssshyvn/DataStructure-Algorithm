T=int(input())

for i in range(T):
  stack=[] # 빈 스택
  string=input()

  for j in string:
    if j=='(':
      stack.append(j)
    else:
      if stack:
        stack.pop()
      else:
        stack.append(j)
        break

  if stack:
    print('NO')
  else:
    print('YES')
