class stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1
    def push(self,data):
        self.tos+=1
        self.arr.append(data)
    def pop(self):
        if self.IsEmpty():
            return
        self.tos-=1
        self.arr.pop()
    def top(self):
        if self.IsEmpty():
            print("Stack is Empty")
            return
        return self.arr[self.tos]
    def size(self):
        return self.tos+1

    def IsEmpty(self):
        return self.tos==-1

def main():
    Stack=stack()
    n=int(input())
    for ele in input().split():
        Stack.push(int(ele))
    print(Stack.size())
    while(Stack.size()!=0):
        print(Stack.top(),end=" ")
        Stack.pop()

if __name__=="__main__":
    main()


# Stack using Linked Lists

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.tos=0
    def push(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tos+=1
            return
        newnode.next=self.head
        self.head=newnode
        self.tos+=1
    def pop(self):
        if self.IsEmpty is True:
            return
        self.head=self.head.next
        self.tos-=1

    def IsEmpty(self):
        if self.head is None:
            return True
        return False
    def Size(self):
        return self.tos
    def Top(self):
        if self.head is None:
            return
        return self.head.data

def main():
    st=Stack()
    for ele in input().split():
        st.push(int(ele))
    print(st.Size())
    for i in range(5):
        print(st.Top(),end=" ")
        st.pop()

if __name__=="__main__":
    main()


#bracket expression
class stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1
    def push(self,data):
        self.tos+=1
        self.arr.append(data)
    def pop(self):
        if self.IsEmpty():
            return
        self.tos-=1
        self.arr.pop()
    def top(self):
        if self.IsEmpty():
            print("Stack is Empty")
            return
        return self.arr[self.tos]
    def size(self):
        return self.tos+1

    def IsEmpty(self):
        return self.tos==-1

def main():
    st=stack()
    
    for i in range(int(input())):
        flag=0
        str=input()
        for ele in str:
            if ele=="(":
                st.push(ele)
            else:
                if (st.IsEmpty()):
                    flag=1
                    break
                st.pop()

        if st.IsEmpty is False or flag==1:
            print("Unstable") 
        else:
            print("stable")   

if __name__=="__main__":
    main()


# bracket Expression for "()""{}""[]"

class stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1
    def push(self,data):
        self.tos+=1
        self.arr.append(data)
    def pop(self):
        if self.IsEmpty():
            return
        self.tos-=1
        self.arr.pop()
    def top(self):
        if self.IsEmpty():
            print("Stack is Empty")
            return
        return self.arr[self.tos]
    def size(self):
        return self.tos+1

    def IsEmpty(self):
        return self.tos==-1

def main():
    st=stack()
    
    for i in range(int(input())):
        flag=1
        str=input()
        for ele in str:
            if (ele=="(" or ele =="[" or ele == "{"):
                st.push(ele)
            else:
                if (st.IsEmpty()):
                    flag=0
                    break
                if((st.top()=="(" and ele==")"  ) or (st.top()=="{" and ele=="}") or (st.top()=="[" and ele==']')):
                    st.pop()
                else:
                    flag=0
                    break

        if st.IsEmpty is False or flag==0:
            print("Unstable") 
        else:
            print("stable")   

if __name__=="__main__":
    main()

#Infix to Postfix
#  
class stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1
    def push(self,data):
        self.tos+=1
        self.arr.append(data)
    def pop(self):
        if self.IsEmpty():
            return
        self.tos-=1
        self.arr.pop()
    def top(self):
        if self.IsEmpty():
            print("Stack is Empty")
            return
        return self.arr[self.tos]
    def size(self):
        return self.tos+1

    def IsEmpty(self):
        return self.tos==-1
def precedence(str):
    if str=="^":
        return 3
    if str=="*" or str =="/":
        return 2
    if str == "+" or str=="-":
        return 1
    if str =="(" or str == ")":
        return -1
    else:
        return 0

def main():
    st=stack()
    arr=list(input().split())
    ans=""
    for i in range(len(arr)):
        val=precedence(arr[i])
        if(val==0):
            ans+=arr[i]
        else:
            if(arr[i]=="("):
                st.push(arr[i])
            elif(arr[i]==")"):
                while(st.IsEmpty() is False and st.top() != "("):
                    ans+=st.top()
                    st.pop()
                if(st.top()=="("):
                    st.pop()
            
            #if arr[i] is an operator
            else:
                while(st.IsEmpty() is False and precedence(arr[i])<=precedence(st.top())):
                    ans+=st.top()
                    st.pop()
                st.push(arr[i])
    while(st.IsEmpty() is False):
        ans+=st.top()
        st.pop()
    print(ans)

if __name__=="__main__":
    main()


# Posfix Expression

class stack:
    def __init__(self):
        self.arr=[]
        self.tos=-1
    def push(self,data):
        self.tos+=1
        self.arr.append(data)
    def pop(self):
        if self.IsEmpty():
            return
        self.tos-=1
        self.arr.pop()
    def top(self):
        if self.IsEmpty():
            print("Stack is Empty")
            return
        return self.arr[self.tos]
    def size(self):
        return self.tos+1

    def IsEmpty(self):
        return self.tos==-1
def IsOP(str):
    if str=="*":
        return 4
    if str =="/":
        return 3
    if str == "-":
        return 2
    if str =="+":
        return 1
    else:
        return 0

def main():
    st=stack()
    n=int(input())
    arr=list(input().split())
    for i in range(n):
        val=IsOP(arr[i])
        if val==0:
            st.push(int(arr[i]))
        else:
            op1=st.top()
            st.pop()
            op2=st.top()
            st.pop()
            if (val==4):
                st.push(op2*op1)
            if (val==3):
                st.push(op2//op1)
            if(val==2):
                st.push(op2-op1)
            if(val==1):
                st.push(op2+op1)
    print(st.top())


if __name__=="__main__":
    main()


def main():
  for t in range(int(input())):
    n=int(input())
    strArr=list(input())
    arr=[]
    res=0
    for ele in strArr:
      if(ele==">" and len(arr)==0):
        break
      if (ele=="<"):
        arr.append(ele)
      elif(ele==">" and len(arr)>0 and arr[-1]=="<"):
        res+=2
        arr.pop()
    print(res)

if __name__=="__main__":
    main()
