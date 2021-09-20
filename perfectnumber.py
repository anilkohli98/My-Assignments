T=int(input())
for T in range(T,0,-1):
 N=int(input())
 sum=0
 for i in range(1,N):
     if N%i==0:
         sum=sum+i
 if sum==N:
     print('true')
 else:
     print("false")

# question according to prepbytes
T=int(input())
while(T>0):
 N=int(input())
 sum=0
 i=1
 while(i<N):
      if N%i==0:
          sum=sum+i
      i=i+1
 if(sum==N):
    print("true")
 else:
    print("false")
 T=T-1

T=int(input())
for T in range(T,0,-1):
  N=int(input())
  count=0
  while(N>0):
    rem=N%10
    N=N//10
    if rem==5:
      count=count+1
  print(count)
 