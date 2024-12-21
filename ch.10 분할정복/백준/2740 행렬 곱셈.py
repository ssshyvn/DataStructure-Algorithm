N, M=map(int, input().split())
A=[list(map(int, input().split())) for i in range(N)]

M, K=map(int, input().split())
B=[list(map(int, input().split())) for i in range(M)]

result=[[0 for i in range(K)] for i in range(N)]

for i in range(N):
  for j in range(K):
    for k in range(M):
      result[i][j]+=A[i][k]*B[k][j]

for i in range(N):
  for j in range(K):
    print(result[i][j], end=' ')
  print()
