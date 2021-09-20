T=int(input())
for T in range(T,0,-1):
    X,Y,K=map(int,input().split())
    total=(X+Y)//K
    print(total)
    if total%2==0:
        print("Shef")
    else:
        print("Paja")

#codechef questions

X,Y=input().split()
X=int(X)
Y=float(Y)
if X<Y:
    if X%5==0:
        total=Y-X-0.50
        print("%.2f"%(total))
    else:
        print("%.2f"%(Y))
else:
    print("%.2f"%(Y))