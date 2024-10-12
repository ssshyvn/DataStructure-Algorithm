# 이진 트리를 위한 노드 클래스
class BTNode:
  def __init__(self, left=-1, right=-1):
    self.left = left    # 왼쪽 자식을 위한 링크
    self.right = right  # 오른쪽 자식을 위한 링크

N=int(input())
tree=[BTNode() for i in range(N+1)]   # [왼쪽 자식, 오른쪽 자식] 형태. 초기값은 [-1, -1]
root_check=[True]*(N+2)   # 각 노드가 루트 노드인지 확인

# 트리 구성
for i in range(N):
  node, left, right=map(int, input().strip().split())
  tree[node]=[left, right]
  if left != -1:
    root_check[left] = True
  if right != -1:
    root_check[right] = True

# 루트 찾기
root=1
for i in range(1, N+1):
  if root_check[i] == False:
    root = i
    break

# 중위순회로 노드의 열 위치 결정
position = 1
level_min = [float('inf')] * (N + 1)      # float('inf'): 양의 무한대
level_max = [0] * (N + 1)

def inorder(node, depth):
    global position
    if node != -1:
      inorder(tree[node][0], depth + 1)                    # 왼쪽 자식
      level_min[depth] = min(level_min[depth], position)   # 현재 노드
      level_max[depth] = max(level_max[depth], position)  
      position += 1
      inorder(tree[node][1], depth + 1)                    # 오른쪽 자식

# 중위 순회 시작
inorder(root, 1)

# 너비가 가장 넓은 레벨 찾기
max_width = 0
max_level = 0

for depth in range(1, N + 1):
    if level_min[depth] != float('inf'):
        width = level_max[depth] - level_min[depth] + 1
        if width > max_width:
            max_width = width
            max_level = depth

# 결과 출력
print(max_level, max_width)
