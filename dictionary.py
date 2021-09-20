#collaction of objects
#mutable
#dynamic(we can inc there size and dec there size)
#this is nested
#in dicrt the objects are accssed by key not by index
ipl_team={
'Mumbai':'Rohit',
'RCB':'Kohli',
'CSK':'Jadeja',
}
print(ipl_team)

#2nd type of writind dictionary

ipl_team={}
ipl_team['DD']='Rishabh Pant'
ipl_team['1']='KOhli'
ipl_team['Bowller']='Bumrah'
ipl_team['CSK']='Raina'
print(ipl_team)

#3rd way to write the dictionary 

ipl_team =dict([
    ("anil","kohli"),
('graduation','btech'),
('currently','unemployed')
])
print(ipl_team)

#conditons for writing the keys

#key is unique duplicate values are no allowed
#if we give the duplicat value than it will overwrite the old value and gives it the latest value
#keys are immutable
#int,float,string,boolean,tuples, can be used as keys because they are immmutable
#dictionary and lists cants be used as keys because they are mutable

#values

#virtually there are no restrictions in values


ipl_team={
'Mumbai':'Rohit',
'RCB':'Kohli',
'CSK':'Jadeja',
'CSK':'Dhoni',
'KKR':'Gambhir'
}
print(ipl_team)#here the duplicate value now it will change the first value with the latest one\
print(type(ipl_team))
print(len(ipl_team))
print(ipl_team)
print(ipl_team.keys())
print(ipl_team.values())
print(ipl_team.items())
print(ipl_team.get('Mumbai'))
print(ipl_team.get('CSK','The key is not present here'))#yaha pr ek mene key dala h or ek default value agr yaha pr key find huyi to ye value print kr dega or ag nhi to ye default value jo ki key is not presnt h vo print krega
a=ipl_team.pop('CSK',"the key is not present")#yaha pr mene ek key pop kr di
print(a,ipl_team)#yaha pr ab key ki value k sath dictionary print hoga
b=ipl_team.popitem()#it imply removes the last item and also it returens the both key and value in paranthises
print(a,b,ipl_team)
del ipl_team['Mumbai']
print(ipl_team)