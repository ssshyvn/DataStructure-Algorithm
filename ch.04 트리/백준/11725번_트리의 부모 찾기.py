from collections import deque

n = int(input().strip())
graph = [[] for _ in range(n + 1)]

# 트리의 연결 정보 저장
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 노드를 저장할 배열
parent = [0] * (n + 1)

# BFS로 부모 노드 찾기
def bfs():
    queue = deque([1])  # 루트 노드가 1번으로 주어짐
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if parent[neighbor] == 0:  # 아직 부모가 정해지지 않은 경우
                parent[neighbor] = current
                queue.append(neighbor)

# BFS 실행
bfs()

# 결과 출력
for i in range(2, n + 1):
    print(parent[i])
