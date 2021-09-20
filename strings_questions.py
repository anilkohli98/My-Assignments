T=int(input())
for T in range(T,0,-1):
  N=int(input())
  A=input("")
  gameA=0
  gameD=0
  if len(A)==N:
    for i in range(N):
      if A[i]=='A':
        gameA+=1
      if A[i]=='D':
        gameD+=1
    if gameA>gameD:
      print("Aditya")
    if gameD>gameA:
      print("Danish")
    if gameD==gameA:
      print("AdiDan")

# vovals 

T=int(input())
for T in range(T,0,-1):
  S=input("")
  A="aeiouAEIOU"
  count=0
  count1=0
  for i in range(len(S)):
    if S[i] in A:
      count+=1
  count1=len(S)-count
  print("%d %d"%(count,count1))
  print(len(S))

#first chacracter

for T in range(int(input())):
  s=input()
  freq=[0]*27
  for i in range(len(s)):
    freq[ord(s[i])-97]+=1
  flag=0
  for i in range(len(freq)):
    flag=0
    if freq[i]==1:
      print(i)
      break
    if freq[i]>1:
      flag+=1
  if flag>=1:
    print(-1)

#first char

def First_NR_Letter(S):
  resunseen=[]
  resseen=[]
  for ele in S:
    if ele in resunseen:
      resunseen.remove(ele)
      resseen.append(ele)
    elif ele in resseen:
      continue
    else:
      resunseen.append(ele)
  if resunseen:
    return S.find(resunseen[0])
  else:
    return -1
for T in range(int(input())):
    print(First_NR_Letter(input()))

#fake password

for T in range(int(input())):
  org=input()
  fake=input()
  lr=fake[2:]+fake[0:2]
  rl=fake[len(fake)-2:]+fake[0:len(fake)]
  if org==lr or rl:
    print("YES")
  else:
    print("NO")

# printing char in decreasing form

for T in range(int(input())):
  s=input()
  freq=[0]*27
  for i in range(len(s)):
    freq[(ord(s[i])-97)]+=1
  for i in range(25,0+1,-1):
      print(freq[i])
      ch=chr(i+97)
      print(type(ch),ch)
  print()

#sorona,iorona Question(codechef)


for T in range(int(input())):
  N,Q=map(int,input().split())
  S=input()
  freq=[0]*26
  for ele in S:
    freq[(ord(ele)-97)]+=1
  for i in range(Q):
    C=int(input())
    count=0
    for j in range(26):
      if freq[j]>C:
        count+=(freq[j]-C)
    print(count)


#good prefix


for T in range(int(input())):
  S=input()
  K,X=map(int,input().split())
  freq=[0]*26
  count=0
  for i in range(len(S)):
    ele=ord(S[i])-97
    freq[ele]+=1
    if freq[ele]>X:
      if K>0:
        freq[ele]-=1
        K-=1
      else:
        break
    else:
      count+=1
  print(count)


#find your gift

for T in range(int(input())):
  N=int(input())
  S=input()
  x=0
  y=0
  cc=''
  if S[0]=='L':
    x-=1
    cc='L'
  elif S[0]=='R':
    x+=1
    cc='R'
  elif S[0]=='U':
    y+=1
    cc='U'
  else:
    y-=1
    cc='D'
  for i in range(1,N):
    if cc=='L' or cc=='R':
      if S[i]=='U':
        y+=1
        cc='U'
      elif S[i]=='D':
        y-=1
        cc='D'
    else:
      if S[i]=='L':
        x-=1
        cc='L'
      elif S[i]=='R':
        x+=1
        cc='R'
  print(x,y)


#Easy subsequence selction

import sys
for T in range(int(input())):
  N=int(input())
  S=input()
  freq=[-1]*26
  min=sys.maxsize
  for i in range(N):
    ele=ord(S[i])-97
    if freq[ele]==-1:
      freq[ele]=i
    else:
      val=i-freq[ele]-1
      print(val)
      freq[ele]=i
      if min>val:
        min=val
        print(min)
  if min==sys.maxsize:
    print(0)
  else:
    print(N-1-min)




import math
def equationSum(N) :
    val=0
    for i in range(1,N+1):
        val+=pow((i+1),2)-(3*i+1)+i
    print(val)
if __name__=='__main__':
    equationSum(int(input()))


def Operations(N) :
   #Enter your code here
   count=0
   while N>0:
       div=N
       while(div>0):
           div=div//10
       N=N-div
       count+=1
   print(count)

print(Operations(int(input())))



#strings question


def main():
  for T in range(int(input())):
    Str1=input()
    Str2=input()
    Freq1=[0]*26
    Freq2=[0]*26
    for j in range(len(Str2)):
      Freq2[ord(Str2[j])-97]+=1
    for i in range(len(Str1)):
      Freq1[ord(Str1[i])-97]+=1
      if (Freq1[ord(Str1[i])-97] and Freq2[ord(Str1[i])-97])>0:
        print(Str1[i]*Freq2[(ord(Str1[i])-97)],end="")
    print()

if __name__=="__main__":
  main()

  #longest substring
  #  
class Solution(object):
   def lengthOfLongestSubstring(self, s):
      i =0
      j = 0
      d={}
      ans = 0
      while j < len(s):
         if s[j] not in d or i>d[s[j]]:
            ans = max(ans,(j-i+1))
            d[s[j]] = j
         else:
            i = d[s[j]]+1
            ans = max(ans,(j-i+1))
            j-=1
         #print(ans)
         j+=1
      return ans
ob1 = Solution()
print(ob1.lengthOfLongestSubstring("abccdefghi"))


def TreeConstructor(strArr):
    parent = []
    child = []

    for i in strArr:
        child.append(int(i[1]))
        parent.append(int(i[3]))
    # each parent node have at most 2 children
    for k,v in Counter(parent).items():
        if v > 2:
            return False
    # each node is unique
    for k,v in Counter(child).items():
        if v > 1:
            return False
    return True

print (TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))      # True
print (TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"] ))      # False