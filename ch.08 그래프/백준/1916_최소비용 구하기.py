INF = 100000001
def getMinVertex():
  minv = 0
  mindist = INF
  for v in range(1, N+1):
    if not visited[v] and mindist > dist[v]:
      mindist = dist[v]
      minv = v
  return minv

def dijkstra(start):
  for v in range(1, N+1):
    dist[v]=graph[start][v]
  visited[start]=True

  for i in range(N-2):
    u=getMinVertex()
    visited[u]=True
    for v in range(1, N+1):
      if not visited[v] and dist[u]+graph[u][v] < dist[v]:
        dist[v]=dist[u]+graph[u][v]
  print(dist[end_city])

N=int(input())
M=int(input())
graph=[[INF for i in range(N+1)] for i in range(N+1)]
dist=[INF for i in range(N+1)]
visited=[False for i in range(N+1)]

for i in range(M):
  start_bus, end_bus, cost=map(int, input().split())
  graph[start_bus][end_bus]=min(graph[start_bus][end_bus], cost)

start_city, end_city=map(int, input().split())
dijkstra(start_city)
