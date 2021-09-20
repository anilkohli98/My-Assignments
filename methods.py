varList=[23,45,5,23,1,2,3,4]
varList.insert(0,47)#iska mtlb index 0 pr mene 47 insert kr diya pr vah pr jo value h vo delete nhi hogi
print(varList)
del varList[0]#jo bhi index 0 pr hoga vo delete ho jayega
print(varList)
varList.reverse()
print(varList)
varList.pop(0)#index 0 pr jo bhi value hogi vo delete ho jayegi but why pop and del are diffrent
print(varList)
a=varList.pop(0)#ab yaha se jo 3 pop hua tha vo 3 mene a m asssign kr diya ye hm esa del m nhi kr skte
print(a,varList)
varList.sort()#yaha pr list ascending m order ho jayegi
print(varList)
#methods of strings
varStr=['A','N','I','L',' ','K','O','H','L','I']#join all the letters
print("".join(varStr))
# varStr.clear()#all the elemrnts are in the list are dleted 
# print(varStr)
NewvarStr=varStr
varStr[0]=223
print('the new list is:\n',NewvarStr)
print('the old list is:\n',varStr)
#there are no changes both the lists are same so for removing this problem
NewvarStr=varStr.copy()#now all the elemnts are in varstr will copy in newvarstr so this will result as changes in both strings
varStr[0]='i Am'
print('the new list is:\n',NewvarStr)
print('the old list is:\n',varStr)
#dictionary methods
mydict={
'anil':'kohli',
1:[5,6,7,8]
}
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.get('anil'))
print(mydict.items())
mydict.pop('anil')
print(mydict)
#fromkeys operator
keyList=[1,3,5,7,9]#ye yaha mene alg se ek list bnayi h
mydict=dict.fromkeys(keyList,1)#ye hr ek list k number k agay 1 likhega or
print(mydict)
mydict=dict.fromkeys(keyList)#yaha list m none print hoga
print(mydict)

#zip operator

pehelazip=['travis','xxx','Anil','fuck']
dusrazip=['Scott','Tentacion','Kohli','Off']
print(zip(pehelazip,dusrazip))#ye yaha sirf location address krega
print(list(zip(pehelazip,dusrazip)))
print(dict(zip(pehelazip,dusrazip)))