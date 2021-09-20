# here is the first method to store an array
from typing import List
arr = []
for ele in input().split():  # for each element of element just split it
    # and append it in array in int form we are converting in int form because input takes data in always string form
    arr.append(int(ele))
for i in range(len(arr)):
    print(arr[i], end=" ")

# here is the 2nd method to convert in array

arr1 = list(map(int, input("enter a number").split()))
# print(arr1)#if we directly do this it will directly print in list
for i in range(len(arr1)):
    print(arr1[i], end=' ')
# question
T = int(input())
for T in range(T, 0, -1):
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == N:
        for i in range(N):
            print(A[i], end=' ')
        print()  # for new line


N = int(input())
A = list(map(int, input().split()))
even=[]
odd=[]
if len(A) == N:
    for i in range(N):
        if A[i] % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])
    for j in range(len(even)):
        print(even[j],end=' ')
    print()
    for k in range(len(odd)):
        print(odd[k],end=' ')