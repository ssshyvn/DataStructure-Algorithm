from collections import deque

n, m = map(int, input().split())
pick = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])      # 양쪽으로 삽입 삭제가 가능한 덱을 사용

count = 0

for i in pick:
    while True:
        if dq[0] == i:      # dq의 첫번째 원소가 현재 pick 원소와 같다면
            dq.popleft()    # 제거 후 break
            break
        else:                               # 같지 않다면 dq에서 현재 pick 원소를 찾아야 함.
            if dq.index(i) < len(dq)/2:     # 현재 pick 원소가 dq의 앞쪽에 있으면 
                while dq[0] != i:           # 앞 원소를 빼서 뒤로 보내는것이 빠르므로, idx가 dq의 맨 앞으로 올 때까지
                    dq.append(dq.popleft()) # 2번 연산 수행 후
                    count += 1              # count 하나 증가

            else:                           # 현재 pick 원소가 dq의 뒤쪽에 있으면 
                while dq[0] != i:           # 뒤 원소를 빼서 앞으로 보내는것이 빠르므로, idx가 dq의 맨 앞으로 올 때까지
                    dq.appendleft(dq.pop()) # 3번 연산 수행 후
                    count +=1               # count 하나 증가

print(count)
