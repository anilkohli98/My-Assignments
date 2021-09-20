def Matrix(A,M):
    for i in range(0,M):
        A.append([int(j) for j in input().split()])   
def main():
    M,N,K=map(int,input().split())
    A= []
    Matrix(A,M)
    for i in range(M):
        for j in range(N):
            print(K*A[i][j], end = " ")
        print()

if __name__=='__main__':
    main()
