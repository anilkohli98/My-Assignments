a,b=map(int,input().split())
#so here if i give the 0 value to b the program stop and give me the error of runtime
#if i want to handle this error and leting the program run and let it to tell the error by itself
#than i will use the blow syntexes
#modulo means the devision first and the remainder is written than

try:#this is use when u feel the error between any lineso every line in which u feels the error u should write under it

    print(a//b)
except Exception as e:#here except is for catching the error and "e" will store the type of error here also the excption is a bigboss class it will handle all he errors like typeerror,value error etc.

    # print("an error has occured")
    print(e) #after all of this the program will not stop abroptly

finally:
    print("printing")

#if there is an error except will execute and if there is no error try will excute and finally will execute in every condition

    

  