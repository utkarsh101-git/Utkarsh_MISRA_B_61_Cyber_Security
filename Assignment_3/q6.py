#6 
f=0
l=list(map(int,input("ENTER THREE NUMBERS BEWTWEEN 1 AND 11\n").split()))
for i in range(0,3):
    if(l[i]>11 or l[i]<1):
        f=1
        print("error")
        break
if(f!=1):
    s=sum(l)
    if s>21:
        if 11 in l:
            s-=10
            if(s>21):
                print("BUST")
            else:
                print(s)
        else:
            print("BUST")
    else:
        print(s)