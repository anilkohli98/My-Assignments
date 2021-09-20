#q.print the different types of data types in one line like
#1.int,2.float(with two numbers after decimals),char with dollar sign btw tham ex 1$2.22$a
i,fl,ch=input("enter the integer,float and character").split()
i=int(i)
fl=float(fl)
print(i,fl,ch)#yaha pr directly ye numbers print kr dega with decimal k piche sirf ek number float ,
#and is print command m hm kuch extra add nhi kr skte like @,$,%,^etc
print("%d$%.2f$%c"%(i,fl,ch))#is print command m %d for int %.2f for float with 2 numbers after decimal and %c for caracter