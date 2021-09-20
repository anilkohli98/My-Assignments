Array=list(map(int,input().split()))
Array.sort()
frequency=[0]*(Array[-1]+1)
count=0
for i in range(len(Array)):
    frequency[Array[i]]+=1
    if frequency[Array[i]]>1:
        count+=1
if count>1:
    print('Array is reapetative')
else:
    print('Elements of Array are not repeating')

#array question
N=int(input())
C=list(map(int,input().split()))
C.sort()
if len(C)==N:
  M=0
  A=[0]*(C[-1]+1)
  print(A)
  for i in range(N):
      A[C[i]]+=1
  for i in range(len(A)):
    if A[i]==1:
      M+=1
  print(M)


#unique colour shift using dict method

N=int(input())
C=[int(ele) for ele in input().split()]
resDict={}
for ele in C:
    if ele in resDict:
        resDict[ele]+=1
    else:
        resDict[ele]=1
print(len([ele for ele in resDict if resDict[ele]==1]))
#here in upper line nothing is happening
#just [ele for ele in resDict if resDict(ele)==1]
#arrTemp=[] #creating a empty list
#for ele in resdict:
#     if reDict(ele)==1 #:than making a condition if resDict(ele)==1
#         arrTemp.append(ele) #than append that element in arrTemp
# print(len(arrTemp)) #and printing the length of that array it will give the unrepeatent numbers