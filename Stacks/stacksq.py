from strings_questions import N, S
class stack:
  def __init__(self):
    self.arr=[]
    self.tos=-1
  def isempty(self):
    if self.tos==-1:
      return True
    return False
  def push(self,data):
    self.arr.append(data)
    self.tos+=1
  def pop(self):
    if self.isempty:
      return -1
    self.arr.pop
    self.tos-=1
  def top(self):
    if self.isempty:
      return -1
    return self.arr[self.toptos+1]
  def getMin(self):
    min=10000000
    if self.top < min:
      min=self.top
    return
  def size(self):
    if self.isempty:
      return -1
    return self.tos + 1
def main():
  st=stack()
  for Q in range(int(input())):
    if Q==1:
      st.push(1)
    x=int(input())
    if Q==3:
      print(st.top())
    if Q==4:
      print(st.getMin())
    if Q==2 or Q ==3 or Q==4:
      if st.isempty():
        print(-1)
      else:
        print(1)
    st.pop()
    
if __name__=="__main__":
  main()


#Stock Question using brute force
  
def main():
  for t in range(int(input())):
    n=int(input())
    span=[1]*n
    price=list(map(int,input().split()))
    for i in range(1,n):
      for j in range(i-1,-1,-1):
        if(price[i]>=price[j]):
          span[i]+=1
        else:
          break
    for ele in span:
      print(ele,end=" ")
    print()
if __name__=="__main__":
  main()

# stock question using optimized aprriach

def main():
  for t in range(int(input())):
    n=int(input())
    span=[1]*n
    price=list(map(int,input().split()))
    st=[]
    st.append(0)
    for i in range(n):
      while(len(st)>0 and price[st[-1]]<=price[i]):
        st.pop()
      if(len(st)<=0):
        span[i]=i+1
      else:
        span[i]=i-st[-1]
      st.append(i)

    for ele in span:
      print(ele,end=" ")
    print()
if __name__=="__main__":
  main()


#sorting of the stack
def insertSorted(stack,value):
  if(len(stack)==0 or value>stack[-1]):
    stack.append(value)
    return
  top=stack.pop()
  insertSorted(stack,value)
  stack.append(top)

def stackSorting(stack):
  if (len(stack)==0):
    return
  top=stack.pop()
  stackSorting(stack)
  insertSorted(stack,top)

def main():
  stack=list(map(int,input().split()))
  stackSorting(stack)
  print(stack)

if __name__=="__main__":
  main()


def main():
  for t in range(int(input())):
    n=int(input())
    strArr=list(input())
    arr=[]
    res=0
    for ele in strArr:
      if (ele=="<"):
        arr.append(ele)
      elif(ele==">" and strArr[-1]=="<"):
        res+=2
        arr.pop()
    print(res)

if __name__=="__main__":
    main()