class node:
    def __init__(self,data):
        self.data=data
        self.next=None

# x=node(1)
# y=node(2)
# z=node(3)
# a=node(4)

# x.next=y
# y.next=z
# z.next=a
# a.next=x
# temp=x
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def InsertAtEnd(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=self.head
            return
        self.tail.next=newnode
        self.tail=newnode
        self.tail.next=self.head

        """
        temp=self.head
        while(True):
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head
            if(newnode.next==self.head):
                break
            temp=temp.next
        """
    def InsertAtBeginning(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=newnode
            return
        newnode.next=self.head
        self.head=newnode
        self.tail.next=self.head

    def InsertAtIPos():
        pass
    def DeletationAtEnd(self):
        if(self.head is None):
            return
        elif(self.head.next is self.head):
            self.head=None
            self.tail=None
            return
        temp=self.head
        while(temp.next is not self.tail):
            temp=temp.next
        self.tail.next=None
        self.tail=temp
        self.tail.next=self.head
    
    def DeletationAtBeginning(self):
        if self.head is None:
            return
        elif(self.head.next is self.tail):
            self.head=None
            self.tail=None
            return
        self.head=self.head.next
        self.tail.next=self.head
    def DeleteAtIPos(self):
        pass
    def PrintingCircularLinkedList(self):
        temp=self.head
        while(True):
            print(temp,temp.data,temp.next)
            temp=temp.next
            if(temp==self.head):
                break
        print()
    
def main():
    List=CircularLinkedList()
    List2=CircularLinkedList()
    A=list(map(int,input().split()))
    for i in range(len(A)):
        List.InsertAtEnd(A[i])
        List2.InsertAtBeginning(A[i])
    List.DeletationAtBeginning()
    List2.DeletationAtEnd()
    List.PrintingCircularLinkedList()
    List2.PrintingCircularLinkedList()

if __name__=="__main__":
    main()