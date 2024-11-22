from queue import Queue

def BFS(start, finish):
  visited=[False]*100001  # 방문 여부 저장 배열

  Q=Queue() # 큐 생성
  Q.put((start, 0))  # 시작 정점(start)과 초기 시간(0초) 큐에 삽입
  visited[start]=True # 시작 정점(start) True로 갱신

  while not Q.empty():
    current, time=Q.get() # 현재 위치와 경과 시간(초)을 큐에서 꺼냄

    # 현재 위치가 동생 위치에 도달하면 시간(초) 반환
    if current==finish:
      return time

    # 현재 위치에서 이동 가능한 세 가지 경우를 큐에 추가
    for next in (current-1, current+1, 2*current):
      if 0 <= next < len(visited) and visited[next] == False:
        visited[next]=True  # 방문 처리
        Q.put((next, time+1)) # 다음 위치와 시간을 큐에 삽입

N, K=map(int, input().split())
print(BFS(N, K))
