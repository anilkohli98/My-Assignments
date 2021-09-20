T=int(input())
for T in range(T,0,-1):
    min=10000001
    max=-1
    N=int(input())
    A=list(map(int,input().split()))
    if len(A)==N:
      for i in range(N):
        if A[i]<min:
          min=A[i]
        if A[i]>max:
          max=A[i]
    # print(min,max)
    print("%d %d"%(min,max))#use for giving the gap
    print("%d%d"%(min,max))#here no gap btw %d%d so no space will given