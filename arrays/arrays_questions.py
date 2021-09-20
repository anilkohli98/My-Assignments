T=int(input())
for T in range(T,0,-1):
    N=int(input())
    arr=list(map(int,input().split()))
    if len(arr)==N:
        arr.sort()
        print(arr[0],arr[-1])
    else:
        False   
