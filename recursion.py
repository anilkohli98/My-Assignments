# Let's start with a simple problem.
# You are given a number 
# N
# , and the task is to find the sum of all numbers from 
# 1
#  to 
# N
# .
# PrepBuddy knowns that using loops you can solve it, he asks you to solve it using recursion.


from sys import setrecursionlimit
setrecursionlimit(10000) 
def Recursive_Sum(N):
    if N==0:
        return 0
    return N+Recursive_Sum(N-1)
for T in range(int(input())):
  Sum=Recursive_Sum(int(input()))
  print(Sum)


# Fibonacci series using Recursion
# Given an integer 
# N
# , your task is to find the 
# N
# t
# h
#  term of Fibonacci series using recursion. First element is considered as 
# 1
#  (one).






# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(9))


#binary with conzecutive 1
def binary_number(n,P,li,i):
  if n==0:
    for j in range(len(li)):
      print(li[j],end='')
    print()
    return
  if P==0 or P==-1:
    li[i]=0
    binary_number(n-1,0,li,i+1)
    li[i]=1
    binary_number(n-1,1,li,i+1)
  else:
    li[i]=0
    binary_number(n-1,0,li,i+1)     
def main():
  for t in range(int(input())):
    n=int(input())
    li=[-1]*n
    binary_number(n,-1,li,0)
if __name__=='__main__':
  main()


#combination of numbers 

def recurComb(arr,op,i,index,n,k):
  if k==0:
    for j in range(len(op)):
      print(op[j],end=' ')
    print()
    return
  for l in range(i,n):
    op[index]=arr[l]
    recurComb(arr,op,l+1,index+1,n,k-1)
#main func
def main():
  for T in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    op=[0]*k
    recurComb(arr,op,0,0,n,k)
#calling func
main()

#removing adjacent elements

def RemAdce(str):
  if len(str)==1:
    return str
  if str[0]==str[1]:
    return RemAdce(str[1:])
  else:
    return str[0]+RemAdce(str[1:])
def main():
  str=input()
  print(RemAdce(str))
main()
  