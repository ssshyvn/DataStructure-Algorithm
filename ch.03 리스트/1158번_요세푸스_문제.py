N, K=map(int, input().split())
answer=[]
arr=[i for i in range(1, N+1)]  # [1, 2, ..., N]
num=0 # 제거 할 인덱스

while len(arr)!=0:
    num+=K-1

    if num>=len(arr):
        num=num%len(arr)
    answer.append(str(arr.pop(num)))

print("<", end="")
print(", ".join(answer), end="")
print(">", end="")
