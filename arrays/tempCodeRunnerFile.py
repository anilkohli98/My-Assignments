
T=int(input())
for T in range(T,0,-1):
  N=int(input())
  A=list(map(int,input().split()))
  if len(A)==N:
    if A[i]>A[i+1]:
      print(i,end=" ")
    if A[N-1]>A[(N-1)-1]:
      print(i,end=" ")
    for i in range(1,N-2):
      if A[i]>A[i-1] and A[i]>A[i+1]:
        print(i,end=" ")
    print()