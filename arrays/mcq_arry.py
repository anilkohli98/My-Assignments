sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)#pop after 2nd element
print(sampleList)

a = [1, 2, 3]
b = a.copy()
print(b is a)#b is just a copy
print(b)

s="a@b@c@d"
a=list(s.partition("@"))
print(a)
b=list(s.split("@",3))
print(b)
#no diff in output
s="a@b@c@d"
a=list(s.partition("@"))
print(a)
b=list(s.split("@"))
print(b)

aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])#here printing the element of 1st index of index 0  
print(aList[1][3])#here 3rd index of 1st index



