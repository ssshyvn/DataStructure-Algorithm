from collections import deque

n = int(input().strip())
if n == 1:  # 노드가 1개인 경우, 지름은 0입니다.
    print(0)
    sys.exit()

# 트리의 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 가장 먼 노드를 찾는 함수 (DFS 사용)
def bfs(start_node):
    distances = [-1] * (n + 1)
    queue = deque([start_node])
    distances[start_node] = 0
    max_distance = 0
    max_node = start_node

    while queue:
        current = queue.popleft()
        current_distance = distances[current]

        for neighbor, weight in graph[current]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드
                new_distance = current_distance + weight
                distances[neighbor] = new_distance
                queue.append(neighbor)
                # 최대 거리 갱신
                if new_distance > max_distance:
                    max_distance = new_distance
                    max_node = neighbor

    return max_node, max_distance

# 첫 번째 BFS 실행: 임의의 노드 1에서 가장 먼 노드 찾기
farthest_node, _ = bfs(1)

# 두 번째 BFS 실행: 가장 먼 노드에서 다시 가장 먼 노드 찾기
_, diameter = bfs(farthest_node)

# 결과 출력
print(diameter)
