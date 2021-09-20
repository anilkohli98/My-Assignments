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