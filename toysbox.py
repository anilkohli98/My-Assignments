testcase=int(input())
count=0
for testcase in range(testcase,0,-1):
    ti,ci=map(int,input().split())
    if (ci-ti)>=2:
        count=count+1
print(count)

#printing star patterns

for T in range(int(input())):
    N=int(input())
    num=(N//2)
    for i in range(1,N+1):
            if i ==(N//2)+1:
                print(' * '*num,' ' ,' * '*num)
            else:
                print(' * '*N)




#dish quistion

def main():
  for T in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    li=[]
    if len(A)==N:
      for i in range(N):
        if A[-1]:
          li.append(A[-1])
          break
        elif (A[i]+1)==A[i+1]:
          continue
        elif (A[i]+1)!=A[i+1]:
          li.append(A[i])
      li.sort()
      print(li[0])
if __name__=='__main__':
  main()