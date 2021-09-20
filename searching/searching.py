#linear search


for T in range(int(input())):
    N=int(input())
    arr=list(map(int,input().split()))
    target=int(input())
    flag=0
    for i in range(N):
        if target==arr[i]:
            print("target is present at index",i)
            flag+=1
            break
    if flag==0:
        print("target is not present") 


#Binary Search(iterative)
def BinarySearch(low,high,A,target):
    flag=0
    while(low<=high):
        mid=low+((high-low)//2)
        if A[mid]==target:
            print(mid)
            flag+=1
            break
        elif A[mid]>target:
            high=mid-1
        else:
            low=mid+1
    if flag==0:
        print(-1)
for T in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    target=int(input())
    BinarySearch(0,N-1,A,target)

#Binary search(Recursive)
def BinarySearch(low,high,A,target):
    if low>high:
        return -1
    mid=low+(high-low)//2
    if A[mid]==target:
        return mid
    elif A[mid]>target:
        return BinarySearch(low,mid-1,A,target)
    elif A[mid]<target:
        return BinarySearch(mid+1,high,A,target)
for T in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    target=int(input())
    res=BinarySearch(0,N-1,A,target)
    if res==-1:
        print(-1)
    else:
        print(res)


#lower bound


def PrintLB(A,N,ele):
    low=0
    high=N
    while(low<high):
        mid=(low+high)//2
        if ele<=A[mid]:
            high=mid
        else:
            low=mid+1
    return low

from sys import setrecursionlimit
setrecursionlimit(100000000)
def main():
    for T in range(int(input())):
        N=int(input())
        A=list(map(int,input().split()))
        for q in range(int(input())):
            ele=int(input())
            print(PrintLB(A,N,ele))

if __name__=="__main__":
    main()

#Upper bound & chocolate question

def PrintUB(A,N,ele):
    low=0
    high=N
    while(low<high):
        mid=(low+high)//2
        if ele>=A[mid]:
            low=mid+1
        else:
            high=mid
    return low

from sys import setrecursionlimit
setrecursionlimit(100000000)
def main():
    for T in range(int(input())):
        N=int(input())
        A=list(map(int,input().split()))
        for q in range(int(input())):
            ele=int(input())
            print(PrintUB(A,N,ele))

if __name__=="__main__":
    main()


#Find Peak Element

def FindPE(A,n,low,high):
    mid=low+(high-low)//2
    if ((mid==0 or A[mid-1]<=A[mid]) and (mid==n-1 or A[mid+1]<=A[mid])):
        return mid
    elif mid>0 and A[mid-1]>A[mid]:
        return FindPE(A,n,low,mid-1)
    else:
        return FindPE(A,n,mid+1,high)

from sys import setrecursionlimit
setrecursionlimit(10000000)
for T in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    res=FindPE(A,n,0,n-1)
    print(A[res])

#for printing the closest divisor to n number basic approach

import math
import sys
n=int(input())
for q in range(int(input())):
    k=int(input())
    temp=0
    mindiff=sys.maxsize
    ans=0
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            temp=abs(k-i)
            if(mindiff>temp):
                mindiff=temp
                ans=i

            if(n//i!=i):
                temp=abs(k-n//i)
                if(mindiff>=temp):
                    mindiff=temp
                    ans=n//i
    print(ans)



def BG(A,B,C,val):
  if (A+(val*C)==B or (A==1 and B>=1 and C==1)) or (A==0 and C==1):
    return 1
  elif(A+(val*C)>B or C==0):
    return 0
  else:
    return BG(A,B,C,val+1)
    
from sys import setrecursionlimit
setrecursionlimit(1000000000)
def main():
    for T in range(int(input())):
        A,B,C=map(int,input().split())
        res=BG(A,B,C,0)
        if res==1:
            print("YES")
        else:
            print("NO")

if __name__=="__main__":
    main()


def BinarySearch(target,arr,low,high,count):
  if low>high:
    return count
  mid=low+(high-low)//2
  if arr[mid]==target:
    count+=1
  elif high>low:
    return BinarySearch(target,arr,low,mid-1,count)
  elif (high!=low and low<high):
    return BinarySearch(target,arr,mid+1,high,count)

from sys import setrecursionlimit
setrecursionlimit(1000000000)

def main():
  for _ in range(int(input())):
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    print(BinarySearch(K,arr,0,N-1,count))

if __name__=="__main__":
    main()