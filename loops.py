
#while loop 

# i,n=map(int,input("enter the two values with space\n").split())
# while(i<=n):
#   print(i)
#   i+=5

# i,n=map(int,input("enter the two values with space\n").split())
# while(i<=n):
#         print(i,end=" ")
#         i+=2
i=1
n=50
while(i<=n):
       if(i==5):
              i+=2
              continue
       print(i,end=" ")
       i+=2
                     
print()
print("loop ended")


              
#for loop

var=range(0,5)
print(var)
print(type(var))

for i in var:#ye for loop k liye use ho raha h
 print(i,"\n")

for i in range(0,20,1):#yaha pr 0 to 20 with increment 1 print honge numbers
       print(i)
for i in range(20,0,-2):              
       print(i)
st="Anil kohli"
for ch in st:
       print(ch)
for i in range(0,len(st)):#yaha pr ye index pr jo value h usko print krega with skip of 0 element 
  print(st[i])

for i in range(0,6):
       for j in range(0,6):
              print("i=",i,"j=",j)  

for i in range(1,6):
       for j in range(i,6):#j is totally depended on i
              print("*",end=" ")
       print()       