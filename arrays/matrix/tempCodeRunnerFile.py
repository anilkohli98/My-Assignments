def main():
  for T in range(int(input())):
    N=int(input())
    mat=[]
    count=0
    for i in range(N):
      mat.append(list(input()))
    li=mat.pop(mat[0])
    print(len(li))
    print(len(mat))
    for i in range(len(li)):
      for j in range(len(mat)):
        if li[i] in mat[j]:
          count+=1

if __name__=='__main__':
  main()