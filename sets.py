VarSet=set("hello")
print(VarSet)
s2=set([1,2,3,4])
print(s2)
st="PrepBytes Is Good"
print(list(st))
print(set(st))
s3={1,2,3,4,"hello"}#this is a set
print(s3)
s4={}#but we cant write a empty set because this will read is as dict
print(type(s4)) 
print(len(s3))
print("a" in s3)

#methods in sets

s1={1,2,3,4,5}
s4={3,4,5,6,7}
s5={1,2,3}
s6={1,2,3,4,5,6,7,8}
print(s1.union(s4))#yaha pr union hoga
print(s1|s4)
print(s1.intersection(s4))
print(s1&s4)#intersection
print(s1.difference(s4))#a k elements print krega jo a m ni h
print(s1-s4)
print(s5.issubset(s1))
print(s5<=s1)
print(s6.issuperset(s1))
print(s6>=s1)

#modification methods

s1.add(6)#yaha ye last m element add kr dwga
print(s1)
s2=s1.copy()
print(s2)

s2.remove(6)
print(s2)
s2.discard(5)
print(s2)
#remove and discard m ye frk h ki remove m agr value di h koi agr vo
#value nhi h set m to von error throw krega discard m esa nhi h 
#ye simply run krta h bs
a=s2.pop()#removes the first element
print(a,s2)

tuple1 = (1, 2, 4, 3) 
tuple2 = (1, 2, 3, 4) 
print(tuple1 < tuple2)


