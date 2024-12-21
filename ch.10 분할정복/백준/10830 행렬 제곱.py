N, B=map(int, input().split())
A=[list(map(int, input().split())) for i in range(N)]

def mulMat(M1, M2):
  tmp=[[0 for i in range(N)] for i in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        tmp[i][j]+=M1[i][k]*M2[k][j]%1000
  return tmp

def powerMat(B):
  if B==1:
    return A
  tmp=powerMat(B//2)
  if B%2==0:
    return mulMat(tmp, tmp)
  else:
    return mulMat(mulMat(tmp, tmp), A)

result=powerMat(B)
for i in range(N):
  for j in range(N):
    print(result[i][j]%1000, end=' ')
  print()
