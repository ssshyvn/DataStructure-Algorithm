# 퀵 정렬 알고리즘
def quick_sort(A, left, right):
  if left<right:    # 정렬 범위가 2개 이상인 경우
    q=partition(A, left, right)   # 피벗을 중심으로 리스트를 두 부분으로 분할하고, 피벗의 위치 q를 구함
    quick_sort(A, left, q-1)      # 왼쪽(left~q-1)과
    quick_sort(A, q+1, right)     # 오른쪽(q+1~right) 부분리스트를 각각 정렬하면 전체 정렬 완료

# 분할 알고리즘 
def partition(A, left, right):
  pivot=A[left]   # 리스트의 가장 왼쪽(left) 요소를 피벗으로 사용하면,
  low=left+1      # low는 left+1이 되고
  high=right      # high는 right가 됨.

  while (low<=high):   # low와 high가 역전되지 않는 한 반복
    while (low<=right and A[low]<=pivot): # A[low]<=피벗 이면
      low+=1                              # low를 오른쪽으로 진행
    while (high>=left+1 and A[high]>=pivot):  # A[high]>피벗 이면
      high-=1                                 # high를 왼쪽으로 진행

    if low<high:      # 역전이 아니면 두 레코드 교환
      A[low], A[high]=A[high], A[low]

  A[left], A[high]=A[high], A[left]   # 마지막으로 피벗과 high를 교환하고,
  return high                         # 피벗의 인덱스 high를 반환

# 출력 
data=[71, 49, 92, 55, 38, 28, 72, 53]
print("Original  : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)
