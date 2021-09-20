li=[1,2,3,4,5]
li1=[2,3,1,5,4]
# for i in range(len(li)):
#     print(li[i])
#     for ele in li:
#         print(ele)
print(li==li1)#gives false because lists are always inn order
li2=[1]#singletun list because it contain only one element

#slicing

li=['a','b','c','d','e','f','g','h','i','j']
l2=li[0:5]#iska mtlb mne yaha a se lekr e tk   value print krani h
print(l2)
print(li[0:])#yaha pr last value t print hoga
print(li[:6])#yaha pr f tk print hoga
print(li[-5:-1])#yaha pr f se lekr i tk print hoga
print(li[-1:-5])#reverse order m print nhi ho skta
print(li[0::2])#it will skip one string from R to L and print it
print(li[::-1])#just if u want to print the list reverse
print(li[::-2])#skip 1 character from R to L and print it

#in and not in operation

print('b' in li)#gives true because b is in list
print("k" not in li)#gives true because k is not in list
print('k' in li)#gives false because k is not in list
#+,* operations

li=li+['k','l']#adding kl in list
print(li)
li=li*2#gives the list 2 times 
print(len(li))#print length
print(min(li))#print min funch acco to ascii vlue
print(max(li))#prints the max value acco to ascii


#lists can be nested 

li=[1,2,3,['anil','kohli',4.6],'Travis','scott',[5,6,7,7.5,['ye','list','k','andr','list h']]]#ye yaha mene list k andr listbna di 
print(len(li))
print(li[3])#ye yaha index 3 pr jo value h vo likhi jayegi
print(li[3][0])#yaha mene list k andr jo list h uske index ko b copy kra diya 
print(li[:len(li)+1])
print(li[6][0:])
print(li[6][4][0::2])
#yaha pr hm negative indexing bhi kr skte h
li.clear()
print(li)
li=[1,2,3,4,5,6,7]
li[-1]=0
print(li)
li[0:4]=[0]#yaha pr 0 se lekr 4 index tk values ko mne 0 put kr diya h
print(li)
print(li+['yekyah',1])#hmaraa add operator list ki each value ko different object m read krta h
li+='ye kya h'#yaha pr bhi +operator ka use kiya h mene
print(li)
li.append('ye kya h')#and jo hmara append h vo value  ko whole object m read krta h
print(li)

#pop insert,remove operator

li=[1,2,3,4,5,6]
print(li)
li.insert(0,0)#isme 0 index pr 0 put huya by shifting the other values
print(li)#yaha pr -1 index m mene 0 add kr diya
li.remove(li[0])#remove m jo bhi object apko remove krna hota h vo likhna hota h na ki idex
print(li)
a=li.pop(0)#pop ka ye fayda h ki ye value return krta h to yaha mene uski return ki huyi va;ue ko a m dala diya h
#so now
print(a,li)