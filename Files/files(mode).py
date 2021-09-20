from os import readlink


f=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\FilesModes.text","w")
t=int(input())
f.write(str(t)+"\n")
while(t!=0):
    n=input()
    f.write(str(n)+"\n")
    t=t-1
f.close()

f=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\FilesModes.text","r")
# print(f.read())#print all the data
# print(f.read(15))#prints 1st 15 char
# print(f.readline())#print 1st line
# print(f.readline())#prints the 2nd line

#if i want that that all line should be print autometically by line by line

# for line in f:
#     print(line,end="")

#readlines methos

# print(f.readlines())#it will read "\n" also output=['6\n', 'Python\n', 'We Are Going To Learn READ methods\n', 'Using VArious Methods\n', 'Lets\n', 'DO\n', 'This\n']

for line in f:
    data=line.split()
    print(data)
    #output
    # ['6']
    # ['Python']
    # ['We', 'Are', 'Going', 'To', 'Learn', 'READ', 'methods']
    # ['Using', 'VArious', 'Methods']
    # ['Lets']
    # ['DO']
    # ['This']   
print(f.read())#now it will not print anything here because all data has been printed previously and 
                #so here the data will be printed from where the prevous were ended.
                # 
f.close()                                             

f=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\FilesModes.text","a")
f.write("\nAppend it")#this string will be added at last with one space after it
