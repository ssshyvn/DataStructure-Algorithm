N=int(input())
tree={}   # dictionary 사용

for i in range(N):
  node, left, right=input().split()
  tree[node]=[left, right]  # node는 key(인덱스) / left, right는 value로 할당 -> {"parent":("left", "right")}

# 전위순회
def preorder(root):
  if root != '.':
    print(root, end='')     # root
    preorder(tree[root][0]) # left
    preorder(tree[root][1]) # right

# 중위순회
def inorder(root):
  if root != '.':
    inorder(tree[root][0])  # left
    print(root, end='')     # root
    inorder(tree[root][1])  # right

# 후위순회
def postorder(root):
  if root != '.':
    postorder(tree[root][0])  # left
    postorder(tree[root][1])  # right
    print(root, end='')       # root

preorder('A')
print()
inorder('A')
print()
postorder('A')
