import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# DFS(깊이 우선 탐색) 함수
def dfs(v):
    visited[v] = True     # 현재 노드를 방문하면 True로 변경
    for i in graph[v]:    # 현재 노드와 연결된 모든 노드 탐색
        if not visited[i]:  # 그 중 방문하지 않은 노드가 있으면
            dfs(i)          # 다시 그 노드부터 탐색 진행

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]  # 인접 리스트(노드 번호가 1부터 시작하므로 인덱스 0은 사용하지 않기 위해 N+1만큼 리스트를 만든다.)
visited = [False] * (N + 1)   # 모든 노드를 False로 초기화

# 그래프 입력 받기
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)  # 무방향 그래프이므로, 양쪽 노드에 서로의 노드를 추가하여 연결
    graph[v].append(u)

# 연결 요소 개수 세기
count = 0
for i in range(1, N + 1): # 노드 1부터 N까지 순회하면서 방문 여부 확인
    if not visited[i]:  # 방문하지 않은 노드가 있다면,
        dfs(i)          # 다시 그 노드부터 탐색 진행
        count += 1      # 이 때 방문하지 않은 노드가 새로운 연결 요소이므로 count를 1 증가 시킴

print(count)
