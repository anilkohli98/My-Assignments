#multiple inheritence is good but u have to awre og on thing that order of the execution 
#this is complax


class car:
    def __init__(self,gears,speed,maxspeed):
        self.gears=gears
        self.speed=speed
        self.maxspeed=maxspeed

    def speedup(self):
        print("speeding up")

    def Break(self):
        print("applying breaks")

class Hyundai:
    def __init__(self):
        self.brandname="Hyundai"#Now here i m not passing the values i m just giving the brandname = hyundayi for each hyundai  car
    
class verna(car,Hyundai):#inheriting both properties to verna car
    #calling the init methods
    def __init__(self, gears, speed, maxspeed):
        car.__init__(self,gears, speed, maxspeed)#self should be written here
        Hyundai.__init__(self)#no arguments to pass thats why the self is used

v1=verna(4,60,250)
print(v1.brandname)
print(v1.gears)
print(v1.speed)
print(v1.maxspeed)