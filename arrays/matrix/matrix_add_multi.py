
#for multiplication
from strings_questions import A


def Addmatrix(M,N,mat1,mat2,AddMat):
  for i in range(M):
    A=[]
    for j in range(N):
      a=0
      a+=mat1[i][j]+mat2[i][j]
      A.append(a)
    AddMat.append(A)
      
def multiMat(M,N,mat1,mat2,mat3):
    for i in range(M):
        A=[]
        for j in range(N):
            a=0
            for k in range(M):
                a+=mat1[i][k]*mat2[k][j]
            A.append(a)
        mat3.append(A) 
def main():
    M,N=map(int,input().split())
    mat1=[]
    mat2=[]
    AddMat=[]
    mat3=[]
    for i in range(0,M):
        mat1.append([int(j) for j in input().split()])
    for i in range(0,N):
        mat2.append([int(j) for j in input().split()])
    Addmatrix(M,N,mat1,mat2,AddMat)
    multiMat(M,N,mat1,mat2,mat3)
    for l in range(M):
        for m in range(N):
            print(AddMat[l][m], end = " ")
        print()
    for i in range(M):
        for j in range(N):
            print(mat3[i][j], end = " ")
        print()

if __name__=='__main__':
    main()

# Aveek sir's logic
def PrintA(mat3,M,N):
  for i in range(M):
    for j in range(N):
      print(mat3[i][j],end=' ')
    print()
  mat3=[]
  for i in range(M):
    mat3.append([0]*N)

M,N=map(int,input().split())

mat1=[]
for i in range(M):
  mat1.append(list(map(int,input().split())))
mat2=[]   
for i in range(M):
  mat2.append(list(map(int,input().split())))
mat3=[]
for i in range(M):
  mat3.append([0]*N)
#addition
for i in range(M):
  for j in range(N):
    mat3[i][j]=mat1[i][j]+mat2[i][j]
PrintA(mat3,M,N)
#for multiplication
for i in range(M):
  for j in range(N):
    for k in range(M):#this loop is for multiplying the row  to collumn so basically this loop is for accessing the elements of columns
      mat3[i][j]=mat3[i][j]+(mat1[i][k]*mat2[k][j])#now here k loop will run M times so when k =o m[0][0]==0,after this mutplication of row 0 and column 1 of mat2 is added to mat[0][0]
      #here the value of mat[0][0] will updateb M times
PrintA(mat3,M,N)
#for upper and lower trianglor matrix

def LowerTriMat(M,N,Arr1):
  K=M-(M-1)
  for i in range(M):
    for j in range(K,N):
        Arr1[i][j]=0
    K+=1
  for i in range(M):
    for j in range(N):
      print(Arr1[i][j],end=" ")
    print()
def UpperTriMat(M,N,A):
  K=1
  for i in range(K,M):
    for j in range(0,K):
      A[i][j]=0
    K+=1
  for i in range(M):
    for j in range(N):
      print(A[i][j],end=" ")
    print()
def main():
    M,N=map(int,input().split())
    A=[]
    Arr1=[]
    for i in range(M):
        A.append([int(j) for j in input().split()])
    for i in range(M):
        a=[]
        for j in range(N):
            a.append(A[i][j])
        Arr1.append(a)
    LowerTriMat(M,N,Arr1)
    UpperTriMat(M,N,A)
if __name__=="__main__":
  main()

#Upper and lower trianglor matrix using class

def Lower_Tri_Mat(mat1,mat2,M,N):
  K=1
  for i in range(M):
    for j in range(K):
      mat2[i][j]=mat1[i][j]
    K+=1
def Upper_Tri_Mat(mat1,mat3,M,N):
  K=0
  for i in range(K,M):
    for j in range(K,N):
      mat3[i][j]=mat1[i][j]
    K+=1
class PrintArr:
  def Mat2(self,mat2,M,N):
    for i in range(M):
      for j in range(N):
        print(mat2[i][j],end=' ')
      print()
  def Mat3(self,mat3,M,N):
    for i in range(M):
      for j in range(N):
        print(mat3[i][j],end=' ')
      print()
def main():
  M,N=map(int,input().split())
  mat1=[]
  for i in range(M):
    mat1.append(list(map(int,input().split())))
  mat2=[]
  for i in range(M):
    mat2.append([0]*N)
  mat3=[]
  for i in range(M):
    mat3.append([0]*N)
  A=PrintArr()
  Lower_Tri_Mat(mat1,mat2,M,N)
  A.Mat2(mat2,M,N)
  Upper_Tri_Mat(mat1,mat3,M,N)
  A.Mat3(mat3,M,N)
if __name__=='__main__':
  main()




  
  