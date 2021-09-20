def BinarySearch(target,arr,low,high,count):
  if low>high:
    return count
  mid=low+(high-low)//2
  if arr[mid]==target:
    count+=1
  elif high>low:
    return BinarySearch(target,arr,low,mid-1,count)
  elif high!=low and low<high:
    return BinarySearch(target,arr,mid+1,high,count)

from sys import setrecursionlimit
setrecursionlimit(1000000000)

def main():
  for _ in range(int(input())):
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    print(BinarySearch(K,arr,0,N-1,count))

if __name__=="__main__":
    main()