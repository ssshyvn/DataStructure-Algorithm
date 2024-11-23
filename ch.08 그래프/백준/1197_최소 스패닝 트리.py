import sys
sys.setrecursionlimit(10**6)

def find(x):
  if parent[x]!=x:
    parent[x]=find(parent[x])
  return parent[x]

def union(a, b):
  a=find(a)
  b=find(b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

V, E=map(int, input().split())
edges=[]
for i in range(E):
  A, B, C=map(int, input().split())
  edges.append((C, A, B))

parent=[i for i in range(V+1)]
edges.sort()
total=0

for c, a, b in edges:
  if find(a)!=find(b):
    union(a, b)
    total+=c

print(total)
