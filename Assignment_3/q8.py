#8
l=list(map(int,input("ENTER THE ELEMENTS OF THE ARRAY").split()))
c=[0,0,7]
ctr=0
for j in range(0,len(l)):
    if(c[ctr]==l[j]):
        ctr+=1
    if(ctr==3):
        break
if(ctr==3):
    print("true")
else:
    print("false")