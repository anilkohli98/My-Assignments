#printing first number
T=int(input())
for T in range(T,0,-1):
  N=int(input())
  while N>0:
    rem=N%10
    N=N//10
  print(rem)

#print sum of digits
X=int(input())
sum=0
while(X>0):
  rem=X%10
  X=X//10
  sum=sum+rem
print(sum)

#printing fav count of fav number 
T=int(input())
for T in range(T,0,-1):
  N=int(input())
  count=0
  while(N>0):
    rem=N%10
    N=N//10
    if rem==5:
      count=count+1
  print(count)

#printing reverse number
X=int(input())
rev=0
while(X>0):
    rem=X%10
    X=X//10
    rev=rev*10+rem
print(rev)
# printing prep Quistion
ch=input()
if ch=="P" or ch=="p":
  print('PrepBytes')
if ch=="Z" or ch=="z":
  print('Zenith')
if ch=="E" or ch=="e":
  print('Expert Coder')
if ch=="D" or ch=="d":
  print('Data Structure')

#printing 2nd smallest
#this code is having error in Y
# X,Y,Z=map(int,input().split())
# if X<Y:
#   smaller1=X
# else:
#   smaller1=Y
# if Y<Z:
#   smaller2=Y
# else:
#   smaller2=Z
# if smaller1<smaller2:
#   print(smaller2)
# else:
#   print(smaller1)

X,Y,Z=map(int,input().split())
if X<=Y<Z or Z<=Y<X:
  print(Y)
if Y<=X<Z or Z<=X<Y:
  print(X)
if X<=Z<Y or Y<=Z<X:
  print(Z)

# printing the pattern of 1
N=int(input())
for i in range(1,6):
    for j in range(1,i+1):
        print(N,end=" ")
    print()

#printing the patteren of 12345

N=int(input())
sum=0
for i in range(5,0,-1):
    sum=0
    for j in range(i,0,-1):
        sum=N+sum
        print(sum,end=" ")
    print()  

#printing  patteren


ch=input()
space=8
for i in range(1,6):
    for j in range(1,i+1):
       print(ch,end="")
    for k in range(space,0,-1):
        print(" ",end="")
    space=space-2
    for j in range(i,0,-1):
      print(ch,end="")
    print()

#toys and box

N=int(input())
count=0
for N in range(1,N+1):
  ti,ci=map(int,input().split())
  if (ci-ti)>=2:
    count=count+1
print(count)

#finding the angles between the cluck nedle

T=int(input())
for T in range(T,0,-1):
  h,m=map(int,input().split())
  hour = (h * 360) // 12 + (m * 360) // (12 * 60)
  min = (m * 360) // 60
#here i use abs function to remove sign
  angle = abs(hour-min)
  if angle > 180:
      angle = 360 - angle
  print(angle)


#question to divisioble by 10
T=int(input())
for T in range(T,0,-1):
  count=0
  N=int(input())
  for i in range(0,1000):
    if N%10==0:
      break
    if N%10!=0:
      count+=1
      N=N*2
  if count<1000:
    print(count)
  else:
    print(-1)

#quantity of a items
N=int(input())
for N in range(N,0,-1):
  quantity,price=map(int,input().split())
  if quantity>100:
    offer=(quantity*price) - (quantity*price*20)/100
    print(offer)
  else:
    print(float(quantity*price))

#finding the number of blocks

T=int(input())
for T in range(T,0,-1):
  M,N=map(int,input().split())
  if M>=0 and N>=0:
    box=M*N//(2*1)
  print(box)
  
#house numbers
#this method is confusing method so i tried string method
T=(int(input()))
for T in range(T,0,-1):
  number_houses=[]
  N=int(input())
  count=0
  div=N//10
  rem=N%10
  for N in range(1,N+1):
    div=N//10
    rem=N%10
    if N<10:
      count+=1
      number_houses.append(count) 
    for i in range(div,0,-1):
      if div>=10:
        rem=div%10
        div=div//10
        number_houses.append(rem)
        number_houses.append
      if N>=10:
        number_houses.append(rem)
      if div<10:
        number_houses.append(div)
        break
  print(len(number_houses))

# using strings
T=int(input())
for T in range(T,0,-1):
  count=0
  house_numbers=[]
  N=int(input())
  for N in range(1,N+1):
    count=int(count)
    count=count+1
    count=str(count)
    house_numbers.append(count)
  house_numbers="".join(house_numbers)
  house_numbers=str(house_numbers)
  print(len(house_numbers))
  print(house_numbers)
  
  #1 at last index

T=int(input())
for T in range(T,0,-1):
    one_index=-1
    N=int(input())
    A=list(map(int,input().split()))
    if len(A)==N:
      for i in range(N):
        if A[i]==1:
          one_index=i
      print(one_index)
    else:
      False


#journey of bablu dablu
for T in range(int(input())):
    N=int(input())
    if(N%8==1):
        print(str(N+3)+"LB")
    elif(N%8==2):
        print(str(N+3)+"MB")
    elif(N%8==3):
        print(str(N+3)+"UB")
    elif(N%8==4):
        print(str(N-3)+"LB")
    elif(N%8==5):
        print(str(N-3)+"MB")
    elif(N%8==6):
        print(str(N-3)+"UB")
    elif(N%8==7):
        print(str(N+1)+"SU")
    elif(N%8==0):
        print(str(N-1)+"SL")
