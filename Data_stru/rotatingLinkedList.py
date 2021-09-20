class node:
  def __init__(self,data):
      self.data=data
      self.next=None
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
    
    def LeftRotate(self,N):
        temp=self.head
        count=1
        while(temp is not None and count<N+1):
            temp=temp.next
            count+=1
        temp2=temp.next
        if (temp2 is None):#this is for the cases like when len ==k
            return
        temp.next=None
        temp2.prev=None
        temp.tail.next=self.head
        self.head.prev=self.tail
        self.head=temp2
        self.tail=temp
            
    def PrintingLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next
        print()

def main():
	List=DoublyLinkedList()
	N,K=map(int,input().split())
	arr=list(map(int,input().split()))
	for i in range(len(arr)):
		List.InsertAtEnd(arr[i])
        # List.InsertAtBeginning(arr[i])
	List.LeftRotate(K)
	List.PrintingLinkedList()

if __name__=="__main__":
    main()