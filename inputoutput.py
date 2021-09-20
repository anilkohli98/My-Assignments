x=input()#ye yaha pr input as a string lega
y=input()#yaha bhi
print(x+y)#yaha pr number add nhi honge yaha pr ye nubers ko sath sath krke likhega kyunki ye as a string le raha h numbr ko
x=int(x)#yha mene string to int m convert kr diya
y=int(y)
print(x+y)#ab yaha addition hogi kyunki ye ab int m h
#agr mujhe direct string ko input vali ek hi line m convert krna h to

a=int(input("enter a number"))#yaha pr hm terminal m space dekr numbers ko sath sath nhi likh skte kyunki ye space ko convert nhi kr payega
b=int(input("enter a number"))#space vali problem ko htane k liye hm split method ka use k6rmge
print(a,b)
#split
X,Y =input().split()#yaha pr split space ko read nhi krega
X=int(X)#yaha pr seprately hme int ko define krna pdega
Y=int(Y)
print(X+Y)
#agr hm sb kuch ek hi line m krna chahte h to 


x,y=map(int,input("enter two numbers").split())
#working of this code is pehele ye numbers ko split krega fir usko map krega x me 
#same process y m hoga
print(x,y)