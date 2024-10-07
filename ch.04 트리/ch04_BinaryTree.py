# 원형 큐: 클래스 정의와 생성자
class ArrayQueue:
    def __init__(self, capacity=10):        # 생성자 정의
        self.capacity = capacity            # 용량(고정)
        self.array = [None] * capacity      # 요소들을 저장할 배열
        self.front = 0                      # 전단 인덱스
        self.rear = 0                       # 후단 인덱스

    # 원형 큐: 공백 상태와 포화 상태 검사
    def isEmpty(self):                      # 공백 상태
      return self.front == self.rear

    def isFull(self):                       # 포화 상태
      return self.front == (self.rear + 1) % self.capacity

    # 원형 큐: 삽입 연산
    def enqueue(self, item):                # 삽입 연산
      if not self.isFull():                 # 포화 상태가 아닌 경우
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
      else:                                 # overflow 처리 X
        pass

    # 원형 큐: 삭제 연산
    def dequeue(self):                      # 삭제 연산
      if not self.isEmpty():                # 공백 상태가 아닌 경우
        self.front = (self.front + 1) % self.capacity
        return self.array[self.front]
      else:                                 # underflow 처리 X
        pass

    # 원형 큐: 상단 들여다보기 연산
    def peek(self):
      if not self.isEmpty():                # 공백 상태가 아닌 경우
        return self.array[(self.front + 1) % self.capacity]
      else:                                 # underflow 처리 X
        pass

    # 원형 큐: 전체 요소의 수
    def size(self):
      return (self.rear - self.front + self.capacity) % self.capacity

    # 원형 큐: 전체 요소를 화면으로 출력
    def display(self, msg):
      print(msg, end='= [')
      for i in range(self.front+1, self.front+1+self.size()):   # front+1부터 size()개의 요소를 순서대로 출력
        print(self.array[i%self.capacity], end=' ')
      print(']')

# 이진 트리를 위한 노드 클래스
class BTNode:
  def __init__(self, elem, left=None, right=None):
    self.data = elem
    self.left = left    # 왼쪽 자식을 위한 링크
    self.right = right  # 오른쪽 자식을 위한 링크

# 이진 트리의 전위순회
def preorder(n):
  if n is not None:
    print(n.data, end=' ')  # 노드를 방문해 처리할 연산들의 위치
    preorder(n.left)        # 왼쪽 서브 트리 처리
    preorder(n.right)       # 오른쪽 서브 트리 처리

# 중첩된 괄호 표현을 위한 전위순회 함수
def preorder_with_parentheses(n):
  if n is not None:
    print("(", n.data, end=' ')  # 현재 노드 데이터와 함께 여는 괄호 출력
    preorder_with_parentheses(n.left)  # 왼쪽 서브 트리 처리
    preorder_with_parentheses(n.right) # 오른쪽 서브 트리 처리
    print(")", end='')  # 현재 노드가 끝나면 닫는 괄호 출력

# 이진 트리의 중위순회
def inorder(n):
  if n is not None:
    inorder(n.left)         # 왼쪽 서브 트리 처리
    print(n.data, end=' ')  # 노드에서 처리할 연산들의 위치
    inorder(n.right)        # 오른쪽 서브 트리 처리

# 이진 트리의 후위순회
def postorder(n):
  if n is not None:
    postorder(n.left)       # 왼쪽 서브 트리 처리
    postorder(n.right)      # 오른쪽 서브 트리 처리
    print(n.data, end=' ')  # 노드에서 처리할 연산들의 위치

# 이진 트리의 레벨 순회
def levelorder(root):
  queue=ArrayQueue()        # 큐 객체 초기화(ArrayQueue 클래스 사용)
  queue.enqueue(root)       # 최초에 루트 노드만 들어있음
  while not queue.isEmpty():# 큐가 공백 상태가 아닌 동안
    n=queue.dequeue()       # 큐에서 하나의 노드를 꺼내고
    if n is not None:       # 이 노드가 None이 아니면 처리
      print(n.data, end=' ')
      queue.enqueue(n.left) # 마지막으로 이 노드의 왼쪽과
      queue.enqueue(n.right)# 오른쪽 자식 노드를 큐에 삽입

# 이진 트리의 노드 수 구하기
def count_node(n):
  if n is None:   # n이 None이면 공백 트리 -> 0을 반환
    return 0
  else:           # 좌우 서브 트리의 노드 수의 합+1 (순환 이용)
    return count_node(n.left) + count_node(n.right) + 1

# 이진 트리의 높이 구하기
def calc_height(n):
  if n is None:   # n이 None이면 공백 트리 -> 0을 반환
    return 0
  hLeft = calc_height(n.left)   # hLeft: 왼쪽 서브 트리의 높이
  hRight = calc_height(n.right) # hRight: 오른쪽 서브 트리의 높이
  if (hLeft > hRight):          # 더 큰 값에 1을 더해 반환
    return hLeft + 1
  else:
    return hRight + 1

# 이진 트리 연산의 테스트 프로그램
d=BTNode('D', None, None)
e=BTNode('E', None, None)
b=BTNode('B', d, e)
f=BTNode('F', None, None)
c=BTNode('C', f, None)
root=BTNode('A', b, c)

print('\n전위 순회: ', end='')
preorder_with_parentheses(root)
print('\n중위 순회: ', end='')
inorder(root)
print('\n후위 순회: ', end='')
postorder(root)
print('\n레벨 순회: ', end='')
levelorder(root)

print("\n노드의 개수 = %d개" %count_node(root))
print("트리의 높이 = %d" %calc_height(root))
