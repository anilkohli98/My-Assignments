#using brute force

T=int(input())
while(T>0):
    N,K=map(int,input().split())
    A=[int(j) for j in input().split()]
    max=-1
    for i in range(N-K+1):
        sum=0
        for j in range(i,i+K):
            sum+=A[j]
        print(sum)
        if max<sum:
            max=sum
    print(max)
    T-=1


#sliding window method
T=int(input())
while(T>0):
    N,K=map(int,input().split())
    A=[int(j) for j in input().split()]
    max=-1
    sum=0
    for i in range(K):
        sum+=A[i]
    for i in range(K,N):
        sum=(sum-A[i-K])+A[i] #here we are removing the 1st element of list and incrementing the element of A[k]
        print(sum)
        if max<sum:
            max=sum
    print(max)
    T-=1


#intersting array
#time limit exceed error because two for loops are using here
T=int(input())
while(T>0):
    N,K=map(int,input().split())
    A=[int(j) for j in input().split()]
    mini=-1
    minj=-1
    if len(A)==N:
        for i in range(N-1): #this is running till  N-1 because here we want to compare elements with the elements but the last element cant be compare with anyone so N-1 is written
            for j in range(N):
                if A[i]+A[j]==K:
                    mini=i
                    minj=j
                elif minj==j and mini>i:
                    mini=i
                    minj=j
    T-=1


#two pointers method
#in case of sorted array
T=int(input())
while(T>0):
    N,K=map(int,input().split())
    A=[int(j) for j in input().split()]
    i=0
    j=N-1
    flag=0
    while(i!=j):
        sum=0
        sum=A[i]+A[j]
        if sum==K:
            flag+=1
            print(i,j)
            break
        elif sum>K:
            j-=1
        else:
            i-=1
    if flag==0:
        print('no answer')
    T-=1

#right number by my method
T=int(input())
for i in range(T,0,-1):
  N=int(input("enter\n"))
  A=[int(j) for j in input("enter\n").split()]
  li=[A[N-1]]
  i=N-1
  j=i
  flag=0
  while(i>=0):
    if A[i] <= A[j]:
        if i==N-1:
            flag+=1
        else:    
            flag=0
            i-=T
            j=i+1
    j+=1
    if flag== 1 or j>N-1:
      print(A[i],end=' ')
      i-=1
      j=i+1
      flag=0
    if A[i]>A[j]:
      flag+=1
  print()

#geeks for geeks method

def printLeaders(A,N):
    
    max_from_right = A[N-1]  
    print(max_from_right)   
    for i in range( N-2, -1, -1):       
        if max_from_right < A[i]:       
            print(A[i])
            max_from_right = A[i]         
def main():
  T=int(input())
  for T in range(T,0,-1):
    N=int(input())
    A=list(map(int,input().split()))
    if len(A)==N:
      printLeaders(A,N)
if __name__=="__main__":
  main()



T=int(input())
for T in range(T,0,-1):
  N=int(input())
  A=list(map(int,input().split()))
  if len(A)==N:
    if A[0]>A[1]:
      print(i,end=" ")
    if A[N-1]>A[(N-1)-1]:
      print(i,end=" ")
    for i in range(1,N-2):
      if A[i]>A[i-1] and A[i]>A[i+1]:
        print(i,end=" ")
    print()

