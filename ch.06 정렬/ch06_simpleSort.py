# 선택 정렬 알고리즘(제자리 정렬 방식)
def selection_sort(A):
  n=len(A)    # 리스트의 크기
  for i in range(n-1):        # i는 정렬되지 않은 부분의 시작 인덱스. 0부터 n-2까지 순서대로 대입.
    least=i
    for j in range(i+1, n):   # i+1부터 n-1까지의 요소 중에서 최솟값의 인덱스 least를 구함.
      if(A[j] < A[least]):
        least=j
    A[i], A[least]=A[least], A[i]   # A[i]와 A[least] 교환
    print(" Step %2d  = "%(i+1), A)   # 단계별 리스트 변화 출력

# 출력
data=[6, 3, 7, 4, 9, 1, 5, 2, 8]
print("Original  : ", data)
selection_sort(data)
print("Selection : ", data) 
