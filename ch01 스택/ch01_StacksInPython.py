# 문자열 역순 출력(파이썬 리스트 이용)
s = list()			            # 리스트 객체를 생성해 스택으로 사용

msg = input("문자열 입력: ")
for c in msg:
    s.append(c)			        # c를 스택에 삽입

print("문자열 출력: ", end='')
while len(s)>0:			        # 스택이 공백 상태가 아니라면
    print(s.pop(), end='')	# 하나의 요소를 꺼내서 출력
print()

# 문자열 역순 출력(LifoQueue 이용)
import queue	                    # 파이썬의 큐 모듈 포함
s = queue.LifoQueue(maxsize=100)	# 스택 객체 생성

msg = input("문자열 입력: ")
for c in msg:
    s.put(c)				              # c를 스택에 삽입
    
print("문자열 출력: ", end='')
while not s.empty():			        # 스택이 공백 상태가 아니라면
    print(s.get(), end='')		    # 하나의 요소를 꺼내서 출력
print()
