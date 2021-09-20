
#without passing the arguments
class student:#class is used to acess the variables
    def __init__(self):#no we are creating an object and we are not paasing it
        self.FirstName="Anil"
        self.LastName="Kohli"
        self.age="22"
s1=student()
s2=student()
print(s1.FirstName,s1.LastName,s1.age)#now both will s1 and s2 prints the same data the data is not pased
print(s2.FirstName,s2.LastName,s2.age)

#with passing the arguments

class student1:
    def __init__(self,FirstName,LastName,Age):#we are creating a object and paasing the argument
        self.FirstName=FirstName
        self.LastName=LastName
        self.age=Age
s1=student1("Anil","Kohli","22")#passing the data from here to arguments like Anil in Firstname,Kohli in Lastname and 22 in age
s2=student1("Nilu","Kohli","22")#same here 
print(s1.FirstName,s1.LastName,s1.age)#now both will have the diff data beacuse we are passing the data
print(s2.FirstName,s2.LastName,s2.age)


#some fuunctions
#like
def print():
    pass
def add():
    pass

#classes and instance

class mobile:
    #class variables are like globle variable
    wireless=True
    Year=2021
    def __init__(self, brandname, color, IsJack):
        #these are the instance variebles
        #which are insinde the init function those are instance
        self.brandname = brandname
        self.color = color
        self.IsJeck = IsJack

    def calling(self):
        print("calling")

    def pictureClick(self):
        print("picture clicked")

    def message(self):
        print("message sent")


def main():
    m1 = mobile("Realme", "blue", True)#this is m1 instance in this the variable values are different 
    print(m1.brandname)
    print(m1.color)
    print(m1.IsJeck)
    m1.calling()
    m1.pictureClick()
    m1.message()
    m1.screen="LED" #we can create new attribute like this
    print(m1.screen)#but this screen atribute is specific of m1 instance only
    print(m1.wireless)#we can use this attribut in both insnace becaus this is a globle variable and  define in a class 
    print(m1.Year)#same for this
    print("------------------------")
    m2 = mobile("Apple", "White", False)#m2 is another instance in which the varieble values are different
    print(m2.brandname)
    print(m2.color)
    print(m2.IsJeck)
    print(m2.wireless)#again we are using this attribute because this attribute is a globle variable
    print(m2.Year)#class level variable 
    # print(m2.screen)#this attribute will  ot work because we do not have this in our template
    m2.brandname="samsung"#we can also create an attribute like this and it will not affact any of attribute
    print(m2.brandname)
    m2.calling()
    m2.pictureClick()
    m2.message()
    mobile.message()#now here it will ask me self paremeter is unfield,so here i have to pass m2 here

#for each instance the values should be different

if __name__ == "__main__":
    main()