testCla = int(input("enter test class\n"))
for testCla in range(testCla,0,-1):
    year = int(input("enter to check leap year\n"))
    if year % 4 == 0:
        if year % 100==0:
            if year%400==0:
                print("yes")
            else:
                print("no")
        else:
            print("yes")        
    else:
        print("no")


#using functions
 
def getLeapyear(year):
    if year % 4==0:
        if year % 100==0:
            if year%400==0:
                print("yes")
            else:
                print("no")    
        else:
            print("yes")
    else:
        print("no")
for _ in range(int(input())):#test cases
    getLeapyear(int(input()))#calling def function 
