import sys
input=sys.stdin.readline

N = int(input())
arr=[0]*10001   # 10001 크기의 리스트 정의

for i in range(N):
  num=int(input())    # 숫자 입력 받기
  arr[num]+=1         # arr 리스트의 num 인덱스 값 1 증가

for i in range(len(arr)):
  if arr[i]!=0:   # arr[i]이 0이 아니면
    for j in range(arr[i]): # 숫자 i(인덱스 번호)가 등장한 횟수만큼
      print(i)              # i(인덱스 번호) 출력
