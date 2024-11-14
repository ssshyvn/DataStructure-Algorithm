# DFS(깊이 우선 탐색) 함수
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# BFS(너비 우선 탐색) 함수
from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력
N, M, V = map(int, input().split())
graph = [[] for i in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 출력
visited = [False] * (N + 1)
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)
