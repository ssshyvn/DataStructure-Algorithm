l_txt=list(input().strip()) # 초기 문자열. 커서 왼쪽에 있는 문자
r_txt=[] # 커서 오른쪽에 있는 문자
M=int(input().strip())

for i in range(M):
  cmd=input().split()

  if 'L' in cmd:
    if l_txt:
      r_txt.append(l_txt.pop())
  elif 'D' in cmd:
    if r_txt:
      l_txt.append(r_txt.pop())
  elif 'B' in cmd:
    if l_txt:
      l_txt.pop()
  elif 'P' in cmd:
    l_txt.append(cmd[1])

l_txt.extend(reversed(r_txt))
print(''.join(l_txt))
