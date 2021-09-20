for T in range(int(input())):
  N,M=map(int,input().split())
  P=list(map(int,input().split()))
  li=[]
  
  if N==len(P):
    i=0
    j=N-1
    sum=0
    while(i<=j):
      if (P[i]<0):
          sum+=P[i]
      elif(j!=i):
          if P[j]<0:
            sum+=P[j]
      i+=1
      j-=1 
    print(abs(sum))


for T in range(int(input())):
  N,M=map(int,input().split())
  P=list(map(int,input().split()))
  li=[]
  if N==len(P):
    i=0
    j=N-1
    sum=0
    while(i<=j):
      if (P[i]<0):
          li.append(P[i])
      elif(j!=i):
          if P[j]<0:
            li.append(P[j])
      i+=1
      j-=1 
    li.sort()
    li.reverse()
    if len(li)>=M:
      for i in range(M):
        sum+=li[i]
    else:
        for i in range(len(li)):
            sum+=li[i]
    print(abs(sum))