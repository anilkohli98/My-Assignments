#tuples
varTup=(3,4.5,3//4)
print(varTup)
varTup=(4,'string',4.5)#you can update tuple
print(varTup)
print("the value at idex 1 is:\n",varTup[1])#yaha pr mene index 1 ki value mangi
print("the value at idex 2 is:\n",varTup[2])
#list
varList=[3,4,5,3]
print(varList)
varList=['gm',4-3,[3,4]]#list k andr hm ek list or bna skte h
print(varList[-1])#ye yaha mene list ka -1 index print kraya
print("second element of -1 index is:\n",varList[-1][1])#yaha pr list k andr list vale ka 2nd element print kiya h
#dictionaries
varDict={}
print(varDict)
varDict={
    "4":4+5,
    4:'anil',
    4:'kohli',
    'list':[1,3,2,4,'list',6,[2,5,4]]    

}
print(varDict['4'])#ye string vala 4 print kiya hmne
print(varDict[4])#dictionary hmesha agr hmne kbhi same keys enter ki h to vo last vali key se pick krega data
print(varDict)
#sets
varSet=set([1,3,4,'anil kohli',4])#duplicate values are not allowed
print(varSet)
varSet=set((2,3,4,3,'duplicate alues not allowed'))#setv k and mene tuple bnaya pr isme hm duplicate values allowed nhi kr skte
print(varSet)
print(varSet[0])#sets m hm index ko print nhi kra skte