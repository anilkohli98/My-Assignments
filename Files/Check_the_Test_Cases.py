f=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\ExpectedOutput.txt","r")
r=open("C:\\Users\\ANIL KOHLI\\Documents\\prepbytes\\Files\\ActualOutput.txt","r")
tescase=0
for line1,line2 in zip(f,r):
    tescase+=1
    if line1==line2:
        print("match")
    else:
        print("WA\nBecause:-")
        print("{}th Test Case Failed".format(tescase))