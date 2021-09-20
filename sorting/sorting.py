#bubblesort
N=int(input())
A=list(map(int,input().split()))
for i in range(N):
  swap=0
  for j in range(N-i-1):
    if (A[j]>A[j+1]):
      A[j],A[j+1]=A[j+1],A[j]
      swap+=1
  if swap==0:
    break
print(A)

#selection Sort
N=int(input())
A=list(map(int,input().split()))
for i in range(N):
    minIndex=i
    for j in range(i+1,N):
        if(A[j]<A[minIndex]):
            A[j],A[minIndex]=A[minIndex],A[j]
print(A)

#insertion sort

for T in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    for i in range(1,N):
        temp=A[i]
        j=i-1
        while(j>-1 and A[j]>temp):
            A[j+1]=A[j]
            j-=1
        A[j+1]=temp
    print(A)
    
#merge sorted array
 
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[0]*(len(a)+len(b))
n,m=len(a),len(b)
i=0
j=0
k=0
while(i<n and j<m):
    if(a[i]<b[j]):
        c[k]=a[i]
        k+=1
        i+=1
    else:
        c[k]=b[j]
        k+=1
        j+=1
while(i<n):
    c[k]=a[i]
    k+=1
    i+=1
while(j<m):
    c[k]=b[j]
    k+=1
    j+=1
print(c)


#merge sort array

def merge(A,l,mid,r):
    n=mid-l+1
    m=r-mid
    A1=[0]*n
    A2=[0]*m
    for i in range(n):
        A1[i]=A[l+i]
    for i in range(m):
        A2[i]=A[mid+1+i]
    i=0
    j=0
    k=l
    while(i<n and j<m):
        if(A1[i]<A2[j]):
            A[k]=A1[i]
            i+=1
            k+=1
        else:
            A[k]=A2[j]
            j+=1
            k+=1
        while(i<n):
            A[k]=A1[i]
            i+=1
            k+=1
        while(j<m):
            A[k]=A2[j]
            j+=1
            k+=1
    print(A)
def mergesort(A,l,h):
    if(l<h):
       mid=l+(h-l)//2
       mergesort(A,l,mid)
       mergesort(A,mid+1,h)
       merge(A,l,mid,h)
    
from sys import setrecursionlimit
setrecursionlimit(100000000)
def main():
    for T in range(int(input())):
        N=int(input())
        A=list(map(int,input().split()))
        mergesort(A,0,N-1)
if __name__=="__main__":
    main()
#partition Algorithm
def partition(A,low,high):
    x=A[high]
    i=low-1
    for j in range(low,high):
        if(A[j]<=x):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return i+1
#quick sort Algorithm
def quicksort(A,low,high):
    if(low<high):
        pi=partition(A,low,high)
        quicksort(A,low,pi-1)
        quicksort(A,pi+1,high)
    

from sys import setrecursionlimit
setrecursionlimit(100000000)
def main():
    for T in range(int(input())):
        N=int(input())
        A=list(map(int,input().split()))
        quicksort(A,0,N-1)
        print(A)
if __name__=="__main__":
    main()



#counting sort algorithm

def CountingSort(A,N):
    K=-1
    for i in range(N):
        if (K<A[i]):
            K=A[i]
        
    freq=[0]*(K+1)
    count=[0]*(K+1)
    B=[0]*N
    for i in range(N):
        freq[A[i]]+=1
    count[0]=freq[0]
    for j in range(K):
        count[j]=count[j-1]+freq[j]
    for k in range(N-1,-1,-1):
        count[A[k]]-=1
        B[count[A[k]]]=A[k]
    print(B)
def main():
    for T in range(int(input())):
        N=int(input())
        A=list(map(int,input().split()))
        CountingSort(A,N)
if __name__=="__main__":
    main()

