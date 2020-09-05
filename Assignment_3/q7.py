#7 till end
l=list(map(int,input("ENTER THE ELEMENTS OF THE ARRAY").split()))
s=sum(l)
deduct=0
for i in range(0,len(l)):
    if(l[i]==6):
        j=i
        while(l[j]!=9and j<len(l)):
            deduct+=l[j]
            j+=1
        s-=(deduct+9)
        i=j
print(s)        
                