
# printing the doubly linked lists

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

# x=node(1)
# y=node(2)
# z=node(3)
# a=node(4)

# x.next=y
# y.prev=x
# y.next=z
# z.prev=y
# z.next=a
# a.prev=z

# temp=x
# while(temp is not None):
#     print(temp.prev,end=" ")
#     print(temp,temp.data,end=" ")
#     print(temp.next)
#     temp=temp.next

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def CountLenRecur(self,temp):
        if temp is None:
          return 0
        else:
          return 1+self.CountLenRecur(temp.next)
    def InsertAtEnd(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            return
        self.tail.next=newnode
        newnode.prev=self.tail
        self.tail=newnode
    def InsertAtBeginning(self,data):
        newnode=node(data)
        if(self.head is None):
            self.head=newnode
            self.tail=newnode
            return
        self.head.prev=newnode
        newnode.next=self.head
        self.head=newnode

    def InsertAtIthPos(self,data,i):
        newnode=node(data)
        n=self.CountLenRecur(self.head)
        if(i==0):
            self.InsertAtBeginning(data)
            return
        elif(i==n):
            self.InsertAtEnd(data)
            return
        elif(i>n):
            print("invalid data")
            return
        count=0
        temp=self.head
        while((temp.next is not None) and count!=(i-1)):
            count+=1
            temp=temp.next
        temp.next.prev=newnode
        newnode.prev=temp
        newnode.next=temp.next
        temp.next=newnode

    def DeletetionAtBeginning(self):
        temp=self.head.next
        self.head.next=None
        temp.prev=None
        self.head = temp
    def DeleteAtEnd(self):
        temp=self.tail.prev
        temp.next=None
        self.tail.prev=None
        self.tail=temp
    def DeleteAtIpos(self,i):
        temp=self.head
        n=self.CountLenRecur(temp)
        if(self.head is None):
            return
        if(i==0):
            self.DeletetionAtBeginning()
            return
        elif(i==n-1):
            self.DeleteAtEnd()
            return
        elif(self.head is None):
            temp.next=None
            temp.prev=None
            temp=None
            self.head=temp
            return
        if(i>n):
            print("invalid value")
            return
        count=0
        while(temp.next is not None and count!=i):
            temp=temp.next
            count+=1
        temp1=temp.prev
        temp2=temp.next
        temp1.next=temp2
        temp2.prev=temp1
        temp.prev=None
        temp.next=None
            
    def PrintingLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next
        print()

def main():
    List=DoublyLinkedList()
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        List.InsertAtEnd(arr[i])
        # List.InsertAtBeginning(arr[i])
    List.InsertAtIthPos(6,4)
    List.PrintingLinkedList()
    List.DeleteAtIpos(3)
    List.PrintingLinkedList()

if __name__=="__main__":
    main()