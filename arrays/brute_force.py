#friend and ages quesstion
N=int(input())
A=list(map(int,input().split()))
freq=[0]*121
for i in range(N):
    freq[A[i]]+=1
ans=0
for i in range(1,121):
    for j in range(1,121):
        if (i<=j*0.5+7):
            continue
        if (i>100 and j<100):
            continue
        if(i>j):
            continue
        ans+=freq[i]*freq[j]
        if i==j:
            ans-=freq[i]
print(ans)

T=int(input())
for T in range(T,0,-1):
  N=int(input())
  A=list(map(int,input().split()))
  A=A*[0]*1
  A.sort()
  print(A)
  freq=[0]*(10000001)
  for i in range(N):
    freq[A[i]]+=1
  ans=0
  for i in range(1,10000000):
    for j in range(1,len(freq)):
      ans+=freq[i]*freq[j]
      if i==j:
        ans-=freq[i]
  print(ans)

li=[1,12,2,3,4]
sum=sum(li)
print(sum)