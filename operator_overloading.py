class student:
    def __init__(self,x,y):#here initializing the values
        self.x=x
        self.y=y
    def __add__(self,other):
        ans1=self.x+other.x#here the addition is like self.x=10 and other.x=30
        ans2=self.y+other.y#here "+" will work because these are working as integers and here the addition is like self.y=20 and other.y=40
        return "{} {}" .format(ans1,ans2)

    def __lt__(self,other):#this function is for calling the smaller function
        ans1=self.x+self.y
        ans2=other.x+other.y
        return ans1+ans2

        if ans1<ans2:
            return True
        else:
            return False

s1=student(10,20)#here s1 is self
s2=student(30,40)#here s2 is other
s3=s1+s2#here "+" will not work  becuase here the s1 and s2 are objects and this "+" is callling the add function for adding
# s3=student.__add__(s1,s2) this line will also work so here we are overloading the operator
print(s3)

if s1<s2:#here "<" is calling __lt__ function
    print("s1 is salller")
else:
    print("s2 is smaller")
