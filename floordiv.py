n=int(input("enter a integer number\n"))
rem=0
while(n>100):
    rem=n%10
    n=n//10
print(rem)

#printinng 1 pattern

for i in range(1,6):
    for j in range(1,i+1):
       print(1,end=" ")
    print()

#in decrese  manner
for i in range(5,0,-1):
    for j in range(i,0,-1):
      print(1,end=" ")
    print()

#in reverse manner

space=4
for i in range(1,6):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    for k in range(i,0,-1):
        print(k,end="")
    print()


    # find the reversed number

num=int(input("enter a number\n"))
revnum=0
while(num>0):
    rem=num%10
    fd=num//10
    revnum=revnum*0+rem
print(revnum,end="")

#test cases\

testcases=int(input())
while(testcases>0):
 x,y=map(int,input("enter the numbers\n").split())
 print(x+y)
 testcases=testcases-1

 
#in v patteren
cha=input()
space=8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(1,space+1):
        print(end=" ")
    space=space-2    
    for j in range(i,0,-1):
        print(j,end="")
    print()    

num=int(input("enter a integer number\n"))
space=10
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(1,space+1):
        print(end=" ")
    space=space-2    
    for j in range(i,0,-1):
        print(j,end="")
    print()

for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
    
