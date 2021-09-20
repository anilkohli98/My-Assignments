tup=(1,2,3,4,4)#this is a packing of tuples
#imutable
#hetrogenius
#used for storing large amount of data
#faster than lists
#baki sb kuch same h lists k jese
print(tup)
v1,v2,v3,v4=tup
print(v1)#this is unpacking of tuples

tup=(1,2,3,4,(1,2,3,4))
print(tup)
print(tup.count(1))#counts the number wit in it
print(tup[4][0:])