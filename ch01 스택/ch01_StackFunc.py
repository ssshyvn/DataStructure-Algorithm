# 스택을 위한 데이터
capacity=100            # 스택 용량
array=[None]*capacity   # 요소 배열
top=-1                  # 상단의 인덱스: 공백 상태(-1)로 초기화

# 스택의 공백 상태와 포화 상태 검사
def isEmpty():
  if top==-1:           # 공백이면 True 반환
    return True
  else:                 # 공백 아니면 False 반환
    return False

def isFull():           # 비교 연산 결과를 바로 반환
  return top==capacity-1

# 스택의 삽입 연산
def push(e):
  global top
  if not isFull():      # 포화상태가 아닌 경우
    top+=1              # top 하나 증가
    array[top]=e        # top 위치에 e 복사
  else:                 # 포화 상태: overflow
    print("stack overflow")
    exit()

# 스택의 삭제 연산
def pop():
  global top
  if not isEmpty():     # 공백 상태가 아닌 경우
    top-=1              # top 하나 감소
    return array[top+1] # 이전(top+1) 위치의 요소 반환
  else:                 # 공백 상태: underflow
    print("stack underflow")
    exit()

# 스택의 peek 연산
def peek():
  if not isEmpty():     # 공백 상태가 아닌 경우
    return array[top]   # top 위치의 요소 반환
  else:                 # underflow 예외 처리 X
    pass

# 스택의 size() 연산
def size():
  return top+1          # 현재 요소의 수는 top+1



msg=input("문자열 입력: ")
for c in msg:
  push(c)

print("문자열 출력: ", end='')
while not isEmpty():
  print(pop(), end='')
print()
