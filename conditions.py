a,b,c=map(int,input('enter the three numbers\n').split())
if(a>b):
 if(a>c):
    print(a,"is the largest")
elif(b>a):   
 if(b>c):
  print(b,"is the largest")
else:
 print(c,"is the largest")

    #combined code

a,b,c=map(int,input('enter the three numbers\n').split())

if(a>b & a>c):
 print(a,"is largest")
elif(b>a & b>c):
 print(b,"is largest")
else:
 print(c,"is largest")



