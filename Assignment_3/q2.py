#2
n1,n2=map(int,input("ENTER THE TWO NUMBERS: ").split())
if(n1%2==0 and n2%2==0):
    print(min(n1,n2))
else: print(max(n1,n2))