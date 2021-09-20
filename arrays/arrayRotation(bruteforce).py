#right rotation using my own method
T=int(input())
for T in range(T,0,-1):
    N,K=map(int,(input().split()))
    A=list(map(int,input().split()))
    if len(A)==N:    
        for i in range(K,0,-1):
            item=A.pop()
            A.insert(0,item)
            print(A)
        for j in range(len(A)):
            print(A[j],end=' ')
    else:
        False

#left rotation using my own method
A=list(map(int,input().split()))
K=int(input())
for i in range(K):
    item=A[0]
    A.remove(A[0])
    print(A)
    A.append(item)
    print(A)
for j in range(len(A)):
    print(A[j],end=' ')

# using function right rotation
def Rightrotation(A,N):
    temp=A[N-1]
    for i in range(N-1,0,-1):
        A[i]=A[i-1]
    A[0]=temp
def printA(A,N):
    for j in range(N):
        print(A[j],end=' ')
    print()
def main():
    T=int(input())
    for T in range(T,0,-1):    
        N,K=map(int,(input().split()))
        A=list(map(int,input().split()))
        if len(A)==N:    
            for i in range(K):
             Rightrotation(A,N)
            printA(A,N)
        else:
            False
if __name__=='__main__':
    main()

#using function leftRotation

def LeftRotation(A,N):
    item=A[0]
    for j in range(N-1):
        A[j]=A[j+1]
    A[-1]=item
def PrintA(A,N):
    for k in range(N):
        print(A[k],end=' ')
    print()
def main():
    T=int(input())
    for T in range(T,0,-1):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        for i in range(K):
            LeftRotation(A,N)
        PrintA(A,N)
if __name__=='__main__':
    main()

#Algo Optimized method
def RightRotAlgo(A,i,j):
  while (i<j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
    i+=1
    j-=1
def PrintA(A,N,K):
  for i in range(N):
      if K>N:
          print(A[i-K],end=' ')
          break
      else:
          print(A[i],end=' ')
  print()
def main():
  T=int(input())
  for T in range(T,0,-1):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    K=K%N
    if K>N:
      PrintA(A,N,K)
    else:
        RightRotAlgo(A,N-K,N-1)
        RightRotAlgo(A,0,N-K-1)
        RightRotAlgo(A,0,N-1)
        PrintA(A,N,K)
if __name__=='__main__':
  main()


#left Rotation


def LeftRotAlgo(A,i,j):
    while(i<j):
        temp=A[i]
        A[i]=A[j]
        A[j]=temp
        i+=1
        j-=1
def PrintA(A,N):
  for i in range(N):
    print(A[i],end=' ')
  print()
def main():
    T=int(input())
    for T in range(T,0,-1):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        LeftRotAlgo(A,0,K-1)
        LeftRotAlgo(A,K,N-1)
        LeftRotAlgo(A,0,N-1)
        PrintA(A,N)
if __name__=="__main__":
    main()       

# Geeks for geeks method for rotation


def RightRotate(a, n, k):
 
    # If rotation is greater
    # than size of array
    k = k % n;
 
    for i in range(0, n):
 
        if(i < k):
 
            # Printing rightmost
            # kth elements
            print(a[n + i - k], end = " ");
 
        else:
 
            # Prints array after
            # 'k' elements
            print(a[i - k], end = " ");
 
    print("\n");
 
# Driver code
Array = [ 1, 2, 3, 4, 5 ];
N = len(Array);
K = 100000;
     
RightRotate(Array, N, K);
 
