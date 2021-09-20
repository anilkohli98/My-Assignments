class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

x=node(1)
y=node(2)
z=node(3)
a=node(4)

x.next=y
y.prev=x
y.next=z
z.prev=y
z.next=a
a.prev=z

temp=x
while(temp is not None):
    print(temp.prev,end=" ")
    print(temp.data,end=" ")
    print(temp.next)
    temp=temp.next