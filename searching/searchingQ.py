#dificulty coding question

# N
#  coders are sitting together wondering whether they should solve an easy problem or a hard problem. They decide to vote. If even a single coder votes for the hard problem then the hard problem has to be solved. But how do they vote? The vote can either be 
# 0
#  or 
# 1
# . If a person votes 
# 0
#  means she/he is voting for the easy problem and 
# 1
#  means a hard problem. 
# Based on 
# N
#  votes, your task is to find whether they will solve the easy or hard problem.

for T in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    flag=0
    for i in range(N):
        if A[i]==1:
            print("hard")
            flag+=1
            break
    if flag==0:
        print("easy") 


for T in range(int(input())):
  N=int(input())
  A=input()
  freq=[0]*26
  for i in range(N):
    freq[ord(A[i])-97]+=1
  print(freq[23])