f=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\ActualOutput.txt","w")
r=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\TestCases.txt","r")
t=int(r.readline().strip())#insted of input we are taking inputs from file
for i in range(t):
    n=int(r.readline().strip())
    data=r.readline().strip()
    arr=list(map(int,data.split()))#moves extra spaces usefull in strings
    min=arr[0]
    ind=None
    for i in range(n):
        if(arr[i]<min):
            min=arr[i]
            ind=i
    f.write(str(ind)+"\n")
    t=t-1