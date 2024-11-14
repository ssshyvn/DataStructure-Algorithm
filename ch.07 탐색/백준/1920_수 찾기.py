# 이진 탐색 함수
def binary_search(arr, key, low, high):
  while low<=high:
    mid=(low+high)//2

    if key==arr[mid]:
      return mid
    elif key>arr[mid]:
      low=mid+1
    else:
      high=mid-1

  return -1

# 입력
N=int(input())
A=list(map(int, input().split()))

M=int(input())
X=list(map(int, input().split()))

# 리스트 A 정렬
A.sort()

# 출력
for i in range(M):
  if binary_search(A, X[i], 0, N-1)!=-1:  # 리스트 A에서 X[i]가 존재하는지 알기 위해서 이진 탐색 진행
    print(1)  # 찾으면 1
  else:
    print(0)  # 못찾으면 0
