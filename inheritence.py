class car:
    def __init__(self,gears,speed,maxspeed):
        self.gears=gears
        self.speed=speed
        self.maxspeed=maxspeed

    def speedup(self):
        print("speeding up")

    def Break(self):
        print("applying breaks")

    def movement(self):#this function is not same for other cars
        print("car moves back and forth")#so i will do here i will overwrite this

class harier(car):#here class car is inheriting in herier class because herier is a car and it should have the same attributes and functions in the class herier
    def race_mode(self):#and also herier is not having any object there
        print("race mode is on")
    def auto_check(self):
        print("system is updating")

class tesla(car):
    def update_check(self):
        print("updating the new software")
    def auto_driving_mode(slef):
        print("auto driving mode is on")
    def airbag(self):
        print("Emergency")
    

h1 = harier(5,60,240)#and herier is asking to put some value in it because herier is not having any init object.herier is a subclass and i am inheriting the values from vcar class
#so i have to put the values here and herier is the sub class of car

print(h1.gears)
print(h1.maxspeed)
print(h1.speed)
h1.speedup()
h1.Break()
h1.race_mode()
h1.auto_check()

print("-------------------------")

h2=tesla(False,70,300)

print(h2.gears)
print(h2.speed)
print(h2.maxspeed)
h2.update_check()
h2.auto_driving_mode()
h2.airbag()

class pal_v(car):
    def movement(self):#for overwriting the name of the function shoul be same
        print("car moves left,right,back and forth")#overwriting the function
    #so if i want to add more attributes in this car than we can also overwrite the attributes
    def __init__(self,mileage,gears,speed,maxspeed):#here i m adding the new attribute to my pal_v1 subclass
        self.mileage=mileage#this mileage is only in the pal_v1 class
        super().__init__(gears,speed,maxspeed)#now here i m passing the other values to simpluy base class
        

print("-------------------------")        

p1=pal_v(16,False,65,300)
print(p1.mileage)
print(p1.gears)
print(p1.speed)
print(p1.maxspeed)

p1.speedup()
p1.Break()
p1.movement()