#5
l=list(map(int,input("ENTER TEH SET OF INTEGERS: ").split()))
f=0
for i in range(0,len(l)):
    if l[i]==3:
        if l[i+1]==3:
            f=1
            print("true")
            break
if(f!=1):
    print("false")