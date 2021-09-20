#no arguments and no return value functions
#this is when we did not pass any arguments in the function and we did not return any value
def addition():
    a,b=map(int,input().split())
    print(a+b)

def main():#main is also a inbuilt function
    addition()#calling a function
    addition()
    addition()

if __name__ == "__main__":
    main()

#Arguments,No return value
#swaping two number
#a,b=b,a
def swap(a,b):
    print(type(a),type(b))
    temp=a[0]
    a[0]=b[0]
    b[0]=temp
    print(a[0],b[0])#remember these a and b are not same as the main function every function is HAVING ITS OWN SCOPE
    #these a and b are of swap function
    #these are swaped

def main():
    a,b=map(int,input("enter the values").split())
    x=[0]*1 #list of one length
    y=[0]*1
    x[0]=a
    y[0]=b
    swap(x,y)#these a and b are of main function these are different than a and b of swap() function
    #these are not swaped 
    print(x[0],y[0])

if __name__ == "__main__":
    main() 

#do  not pass arguments,return value

# value and execution is over for a function it will always return a value to its calling point
#whether it is returning or not it will always return a value to its calling point

def addition_ret():
    a,b=map(int,input().split())
    return (a+b)
def main():
    addi=addition_ret()#calling and assigning the variable
    print(addi)

if __name__=="__main__":
    main()