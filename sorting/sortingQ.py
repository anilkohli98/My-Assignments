#Median of Sorted Array
# Sorting is another very important concept in competitive programming. Many of the problems can be solved easily if the elements are arranged in sorted order. We are going to solve one such problem. 
# We all have studied the median in our schools, it is a simple concept. Let's say we have 
# N
#  numbers arranged in sorted order. Median is nothing but the mid element in case of an odd number of elements and in case of even number of elements it is the average of the two mid elements.

# To keep your task simple, we have kept 
# N
#  as odd for you. So, your task is to find the median among 
# N
#  elements.
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
  N=int(input())
  A=list(map(int,input().split()))
  quicksort(A,0,N-1)
  print(A[(N-1)//2])
if __name__=="__main__":
    main()

# Tina and Rahul have got 
# N
#  bags of chocolates. Both of them love chocolates and want to get the maximum number of chocolates for themselves. So, they came up to an agreement of choosing chocolate bags. They will take the chocolate bags in turns. In each turn, one of them can choose one of the remaining bags and keep it with herself/himself.

# PrepBuddy wants to know the maximum number of chocolates that can Tina collect assuming that Tina takes the first turn.


def partition(A,low,high):
    x=A[high]
    i=low-1
    for j in range(low,high):
        if(A[j]<=x):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return i+1
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
    flag=0
    Choco=0
    for i in range(N):
      flag+=1
      if(flag%2!=0):
        Choco+=A[-1]
        A.remove(A[-1])
      elif(flag%2==0):
        A.remove(A[-1])
    print(Choco)
    
if __name__=="__main__":
  main()


# Rahul and Tina have collected a few stones. They are given an array and are asked to arrange the stones in an array according to their weights. Tina is given the first half of the array and she arranges weight of stones in increasing order and Rahul does the same task for his stones in 2nd half of the array.

# Now PrepBuddy wants you to completely sort this array from start to end containing weight of stones placed.

def partition(A,low,high):
    x=A[high]
    i=low-1
    for j in range(low,high):
        if(A[j]<=x):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return i+1
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
    for i in range(N):
      print(A[i],end=" ")
    print()
if __name__=="__main__":
    main()

# Some problems are like a mirage. They seem to have a different solution when you see it first but as you deep dive you realize the solution is something else.

# Next, we are going to solve one such problem.

# You are given an array consisting of 0's, 1's and 2's. Your task is to sort the array.

def partition(A,low,high):
    x=A[high]
    i=low-1
    for j in range(low,high):
        if(A[j]<=x):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return i+1
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
    for i in range(N):
      print(A[i],end=" ")
    print()
if __name__=="__main__":
    main()




# Mathematics marks of 
# N
#  students are arranged in an array and two teachers are forming a team each for Maths Olympiad. 
# They select students turn wise, in each turn, they select a student marks and removes it from the array. This goes on until only one mark is left in the array. Considering teacher1 takes the first turn, can you tell us which mark will be left in the array after 
# N
# −
# 1
#  turns.

# Initially, there are 
# N
#  integers written on the board. Each turn a player selects one number and erases it from the board. This continues until there is only one number left on the board, i.e. 
# N
# −
# 1
#  turns are made. The first player makes the first move, then players alternate turns.

# The first player wants to minimize the last number that would be left on the board, while the second player wants to maximize it.

# You want to know what number will be left on the board after 
# N
# −
# 1
#  turns if both players make optimal moves.


def partition(A,low,high):
    x=A[high]
    i=low-1
    for j in range(low,high):
        if(A[j]<=x):
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return i+1
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
    flag=0
    for i in range(N):
      flag+=1
      if(len(A)>1 and flag%2!=0):
        A.remove(A[-1])
      elif(len(A)>1 and flag%2==0):
        A.remove(A[0])
      else:
        print(A[0])
if __name__=="__main__":
    main()


# Arnab is given an array of integers of size 
# N
# . His teacher asked Arnab to sort the array but as usual, Arnab did not do his task. So now the teacher will cut his marks for each misplaced element. Arnab wants to know how much marks he will lose.

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
  for t in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    B=A.copy()
    quicksort(A,0,N-1)
    flag=0
    for i in range(N):
      if A[i]!=B[i]:
        flag+=1
    print(flag)
if __name__=="__main__":
    main()


#inversion of array question


def merge(A,l,mid,r):
    n=mid-l+1
    m=r-mid
    A1=[0]*n
    A2=[0]*m
    for i in range(n):
        A1[i]=A[l+i]
    for i in range(m):
        A2[i]=A[mid+1+i]
    inv_count=0
    i=0
    j=0
    k=l
    while(i<n and j<m):
        if(A1[i]<=A2[j]):#changes are made here
            A[k]=A1[i]
            i+=1
            k+=1
        else:
            A[k]=A2[j]
            inv_count+=(n-i)
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
    return inv_count
def mergesort(A,l,h):
    inv_count=0
    if(l<h):
       mid=l+(h-l)//2
       inv_count+=mergesort(A,l,mid)
       inv_count+=mergesort(A,mid+1,h)
       inv_count+=merge(A,l,mid,h)
    return inv_count
    
from sys import setrecursionlimit
setrecursionlimit(100000000)
def main():
    for _ in range(int(input())):
        N=int(input())
        A=list(map(int,input().split()))
        print(mergesort(A,0,N-1))
if __name__=="__main__":
    main()



#Find the window


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