
# The best way to master Linked list is to start with basics. Let's solve one such basic question. Given a linked list you have to print the middle element. Finding a middle element in an array is a matter of accessing an element using its index but in this case, you might have to do some linked list traversal.
# Let the number of elements in the list be 
# N
# .
# If 
# N
#  is odd simply print the mid element, else print element at 
# (
# N
# /
# 2
# )
# +
# 1
#  position

# Complete the printMidElement() function below
# For your reference



#Reverse the Linked List

from typing import Reversible


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
    return count

  def Reverse(self):
	  curr=None
	  prev=None
	  next=None
	  curr=self.head
	  self.tail=self.head
	  while(curr is not None):
		  next=curr.next
		  curr.next=prev
		  prev=curr
		  curr=next
	  self.head=prev
  def ReverseRecur(self,curr,prev):
	  self.tail=self.head
	  if (curr is None):
		  self.head=prev
		  return
	  next=curr.next
	  curr.next=prev
	  self.ReverseRecur(next,curr)
  def PrintingLinkedlist(self):
	  temp=self.head
	  while(temp is not None):
		  print(temp,temp.data,temp.next)
		  temp=temp.next

def main():
  singlyLnkedList=linkedList()
  arr=list(map(int,input().split()))
  for i in range(len(arr)):
    singlyLnkedList.InsertAtEnd(arr[i])
#   singlyLnkedList.Reverse()
  singlyLnkedList.ReverseRecur(singlyLnkedList.head,None)
  singlyLnkedList.PrintingLinkedlist()
  print(singlyLnkedList.tail,singlyLnkedList.tail.data)

if __name__=="__main__":
  main()

#rotating a doubly linked list by k elements
	   
	# remove pass and then write your code


