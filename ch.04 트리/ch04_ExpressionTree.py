# 이진 트리를 위한 노드 클래스
class BTNode:
  def __init__(self, elem, left=None, right=None):
    self.data = elem
    self.left = left    # 왼쪽 자식을 위한 링크
    self.right = right  # 오른쪽 자식을 위한 링크

  # 단말노드
  def isLeaf(self):
    return self.left is None and self.right is None

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

# 수식 트리 계산 함수
def evaluate(node):
    if node is None:      # 공백 트리이면 0 반환
        return 0
    elif node.isLeaf():   # 단말노드이면 -> 피연산자
        return node.data  # 그 노드의 값(데이터) 반환
    else:                 # 루트나 가지노드라면 -> 연산자
        op1 = evaluate(node.left)   # 왼쪽과 오른쪽 서브트리를 먼저 계산해야 루트를 계산할 수 있음.
        op2 = evaluate(node.right)
        if node.data == '+':       # 루트(현재 노드)를 처리. 후위순회
            return op1 + op2
        elif node.data == '-':
            return op1 - op2
        elif node.data == '*':
            return op1 * op2
        elif node.data == '/':
            return op1 / op2

# 후위표기 수식을 이용한 수식 트리 만들기
def buildETree(expr):     # 후위표기 수식을 expr로 전달
  if len(expr)==0:
    return None

  token=expr.pop()        # 후위순회는 수식을 뒤에서 앞으로 처리. 따라서 pop()으로 맨 뒤의 요소를 꺼냄.
  if token in ['+','-','*','/']:  # 연산자이면 노드를 만들고, 오른쪽과 왼쪽순으로 서브트리를 순환호출을 이용해 만듦.
    node=BTNode(token)
    node.right=buildETree(expr)
    node.left=buildETree(expr)
    return node                   # 마지막으로 노드 반환
  else:                           # 피연산자이면 단말노드이므로 노드를 만들어 바로 반환
    node=BTNode(token)
    return BTNode(float(token))

# 수식 트리 테스트 프로그램
str=input("입력(후위표기): ")
expr=str.split()
print("토큰분리(expr): ", expr)
root=buildETree(expr)
print("\n전위순회: ", end="")
preorder_with_parentheses(root)
print("\n중위순회: ", end="")
inorder(root)
print("\n후위순회: ", end="")
postorder(root)
print("\n계산 결과: ", evaluate(root))
