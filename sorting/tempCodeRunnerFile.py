def main():
  t=int(input())
  while(t!=0):
    n=int(input())
    a=list(map(int,input().split()))
    start=0
    end=n-1
    while(start<n-1):
      if(a[start]>a[start+1]):
        break
      start+=1
    while(end>0):
      if(a[end<a[end-1]]):
        break
      end-=1
    print(start,end)
    a2=a[start:end+1]
    print(a2)

    a2.sort()
    print(a2)
    min=a2[0]
    max=a2[-1]
    print(min,max)
    for i in range(start):
      if (a[i]>min):
        start=i
    for j in range(end,n):
      if(a[j]<max):
        end=j
    print(start,end)
    t-=1
  
if __name__=="__main__":
  main()