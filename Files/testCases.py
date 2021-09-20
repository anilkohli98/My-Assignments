
# this is how we generate th testcases

import random
f=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\TestCases.txt","w")
t=10
f.write(str(t)+'\n')
for i in range(t):
    size=random.randrange(1,10)
    f.write(str(size)+"\n")
    for j in range(size):
        ele=random.randrange(0,10)
        f.write(str(ele)+" ")
    f.write("\n")