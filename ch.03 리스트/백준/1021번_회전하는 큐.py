from collections import deque

n, m = map(int, input().split())
p = list(map(int, input().split())) #뽑으려는 수위치
dq = deque([i for i in range(1, n+1)])

count = 0

for i in p:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count +=1

print(count)
