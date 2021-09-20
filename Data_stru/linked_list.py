from _typeshed import Self


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
x=node(10)
y=node(20)
x.next=y
y.next=None
print(y)
print(y.next)
print(x.data)
print(y.data)
print(x.next.data)

#Printing the linked list using(insert at end)
class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None
  def InsertAtEnd(self,data):
    Newnode=node(data)
    print(data)
    print(Newnode)
    print(self.head)
    if (self.head is None):
      self.head=Newnode
    
    else:
      temp=self.head
      print(temp)
      while(temp.next is not None):
        print(temp.next)
        temp=temp.next
        print(temp)
      temp.next=Newnode

  def PrintingLinkedList(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      print(temp, end=" ")
      print(temp.next)
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  singlyLnkedList.PrintingLinkedList()

if __name__=="__main__":
  main()

#insersion at end using tail

class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None
      self.tail=None


  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
      self.tail=Newnode
    
    else:
      self.tail.next=Newnode
      self.tail=Newnode



  def PrintingLinkedList(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      print(temp, end=" ")
      print(temp.next)
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  singlyLnkedList.PrintingLinkedList()

if __name__=="__main__":
  main()



#insersion at beggining

class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None
      self.tail=None


  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
      self.tail=Newnode
    
    else:
      self.tail.next=Newnode
      self.tail=Newnode

  def InsertAtBegening(self,data):
    Newnode=node(data)
    if(self.head is None):
      self.head=Newnode

    else:
      Newnode.next=self.head
      self.head=Newnode




  def PrintingLinkedList(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      print(temp, end=" ")
      print(temp.next)
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtBegening(arr[i])
  singlyLnkedList.PrintingLinkedList()

if __name__=="__main__":
  main()


# insert at i possition starting from 0

class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None
      self.tail=None


  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
      self.tail=Newnode
    
    else:
      self.tail.next=Newnode
      self.tail=Newnode

  def InsertAtBegening(self,data):
    Newnode=node(data)
    if(self.head is None):
      self.head=Newnode

    else:
      Newnode.next=self.head
      self.head=Newnode

  def insertAtI(self,i,data):
    newnode=node(data)
    if(i==0):
      self.InsertAtBegening(data)
    else:
      count=0
      temp=self.head
      while(temp.next is not None and count!=(i-1)):
        count+=1
        temp=temp.next
      if(temp.next is None and i>(count+1)):
        return
      else:
        newnode.next=temp.next
        temp.next=newnode




  def PrintingLinkedList(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      print(temp, end=" ")
      print(temp.next)
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  I,P=map(int,input().split())
  singlyLnkedList.insertAtI(I,P)
  singlyLnkedList.PrintingLinkedList()
if __name__=="__main__":
  main()


# count the length of linked list

class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None

  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
    
    else:
      temp=self.head
      while(temp.next is not None):
        temp=temp.next
      temp.next=Newnode

  def CountLen(self):
    count=0
    temp=self.head
    while(temp is not None):
      count+=1
      temp=temp.next
    print(count)

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  singlyLnkedList.CountLen()

if __name__=="__main__":
  main()

#count length using recursion

class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None

  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
    
    else:
      temp=self.head
      while(temp.next is not None):
        temp=temp.next
      temp.next=Newnode

  def CountLenRecur(self,temp):
    if temp is None:
      return 0
    else:
      return 1+self.CountLenRecur(temp.next)
    

from sys import setrecursionlimit
setrecursionlimit(100000000)

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  temp=singlyLnkedList.head
  print(singlyLnkedList.CountLenRecur(temp))

if __name__=="__main__":
  main()


#printing the data value at i possion


class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None
      self.tail=None


  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
      self.tail=Newnode
    
    else:
      self.tail.next=Newnode
      self.tail=Newnode

  def InsertAtBegening(self,data):
    Newnode=node(data)
    if(self.head is None):
      self.head=Newnode

    else:
      Newnode.next=self.head
      self.head=Newnode

      
  def PrintingLinkedList(self,i):
    count=0
    temp=self.head
    while(temp is not None and count<=i):
      if(count==i):
        print(temp.data)
        break
      else:
        count+=1
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  I=int(input())
  singlyLnkedList.PrintingLinkedList(I)
if __name__=="__main__":
  main()


# Deletetion at end


class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None

  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
    
    else:
      temp=self.head
      while(temp.next is not None):
        temp=temp.next
      temp.next=Newnode
    
  def DeletationAtEnd(self):
    if(self.head is None):
      return
    elif(self.head.next is None):
      self.head=None
    else:
      sl=self.head
      while(sl.next.next is not None):
        sl=sl.next
      self.tail=sl
      sl.next=None

  def PrintingLinkedList(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      print(temp, end=" ")
      print(temp.next)
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  singlyLnkedList.DeletationAtEnd()
  singlyLnkedList.PrintingLinkedList()

if __name__=="__main__":
  main()


#deletation at the beggining

class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None

  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
    
    else:
      temp=self.head
      while(temp.next is not None):
        temp=temp.next
      temp.next=Newnode
    
  def DeletationAtBegining(self):
    if(self.head is None):
      return
    else:
      self.head=self.head.next
    

  def PrintingLinkedList(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      print(temp, end=" ")
      print(temp.next)
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  singlyLnkedList.DeletationAtBegining()
  singlyLnkedList.PrintingLinkedList()

if __name__=="__main__":
  main()


#deleting at the i th possion

class node:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class linkedList:
  def __init__(self):
      self.head=None

  def InsertAtEnd(self,data):
    Newnode=node(data)
    if (self.head is None):
      self.head=Newnode
    
    else:
      temp=self.head
      while(temp.next is not None):
        temp=temp.next
      temp.next=Newnode
  def CountLenRecur(self,temp):
    if temp is None:
      return 0
    else:
      return 1+self.CountLenRecur(temp.next)
    
  def DeletationAtBegining(self):
    if(self.head is None):
      return
    else:
      self.head=self.head.next

  def DeletationAtEnd(self):
    if(self.head is None):
      return
    elif(self.head.next is None):
      self.head=None
    else:
      sl=self.head
      while(sl.next.next is not None):
        sl=sl.next
      self.tail=sl
      sl.next=None
  def DeleteAtIPos(self,k,N):
    if(self.head is None or k>N-1):
      return
    if(k==0):
      self.DeletationAtBegining()
  
    elif(k==N-1):
      self.DeletationAtEnd()
    else:
      count=0
      temp=self.head
      while(count<k):
        if(count==k-1):
          temp.next=temp.next.next
        else:
          temp=temp.next
        count+=1

  def DeleteAtIPosByPrep(self,k,N):
    if (self is None or k>N-1):
      return
    if(k==0):
      self.DeletationAtBegining()
    elif(k==N-1):
      self.DeletationAtEnd()
    else:
      count=0
      temp=self.head
      while(self.head is not None and count is not (k-1)):
        count+=1
        temp=temp.next
      temp.next=temp.next.next 
  def PrintingLinkedList(self):
    temp=self.head
    while(temp is not None):
      print(temp.data,end=" ")
      print(temp, end=" ")
      print(temp.next)
      temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  k=int(input())
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
  temp=singlyLnkedList.head
  N=singlyLnkedList.CountLenRecur(temp)
  singlyLnkedList.DeleteAtIPos(k,N)
  singlyLnkedList.PrintingLinkedList()
  singlyLnkedList.DeleteAtIPosByPrep(k,N)
  singlyLnkedList.PrintingLinkedList()

if __name__=="__main__":
  main()