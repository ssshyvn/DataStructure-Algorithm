N, K=map(int, input().split())
answer=[]
circle=[i for i in range(1, N+1)]  # [1, 2, ..., N] -> 원형 큐 사용
num=0 # 몇번째 사람을 제거할건지

while len(arr)!=0:
    num+=K-1    # 제거할 인덱스 설정(0부터 시작해야 함)

    if num>=len(arr):       # 인덱스가 남아있는 배열 길이보다 클 경우
        num=num%len(arr)    # 다시 맨 앞으로 돌아가야 함
    answer.append(str(arr.pop(num)))

print("<", end="")
print(", ".join(answer), end="")
print(">", end="")
