A, B, C=map(int,input().split())

def power(A, B):
  if B==1:
    return A%C
  tmp=power(A, B//2)
  if B%2==0:
    return tmp*tmp%C
  else:
    return tmp*tmp*A%C

print(power(A, B))
