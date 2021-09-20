class jiocaller():
    def call(self):
        print("calling")#function is calling
class truecaller():
    def call(self):#here i m defining call function
        print("ringing")
        print("Caller data")

class phone:
    def callfunc(self,phoneapp):#so here i m making a calling function in this function i need a app which uses for a call so phoneappn is there for a call
        phoneapp.call()#so using this phone app i m calling

# phoneapp=truecaller()#i create a instance of a truecaller phoneapp 
phoneapp=jiocaller()
p1=phone()#here i created a instance of a phone
p1.callfunc(phoneapp)#phoneapp is an object which is accessing the call function of truecaller
#so here the outcome is that i dont care about these two apps if my function is working for calling
