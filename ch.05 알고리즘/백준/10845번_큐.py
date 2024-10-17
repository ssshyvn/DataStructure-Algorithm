import queue
import sys
input=sys.stdin.readline

q=queue.Queue() # 큐 객체 생성
N=int(input())

for i in range(N):
  order=input().split() # 문자열을 입력받아 공백으로 나눔

  if order[0]=='push':
    q.put(order[1])

  elif order[0]=='pop':
    if q.empty():
      print(-1)
    else:
      print(q.get())

  elif order[0]=='size':
    print(q.qsize())

  elif order[0]=='empty':
    if q.empty():
      print(1)
    else:
      print(0)

  elif order[0]=='front':
    if q.empty():
      print(-1)
    else:
      print(q.queue[0])

  elif order[0]=='back':
    if q.empty():
      print(-1)
    else:
      print(q.queue[len(q.queue)-1])
