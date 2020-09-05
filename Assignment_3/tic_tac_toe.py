def check(l):
    if(l[0]==l[1]==l[2]):
        return 1
    elif(l[3]==l[4]==l[5]):
        return 1
    elif(l[6]==l[7]==l[8]):
        return 1
    elif(l[0]==l[3]==l[6]):
        return 1
    elif(l[1]==l[4]==l[7]):
        return 1
    elif(l[2]==l[5]==l[8]):
        return 1
    elif(l[0]==l[4]==l[8]):
        return 1
    elif(l[2]==l[4]==l[6]):
        return 1
    else:
        return 0
def display(l):
    print()
    for i in range(0,len(l)):
        if((i+1)%3==0):
            print(l[i])
            if(i!=8):
                print("---------")
        else:
            print(l[i],"|",end=" ")
    print()        
    return 1    
def inputing(p):
    print("CHOICE FOR PLAYER 1\n Press 1 for X \n press 2 for O")
    n=int(input("Enter your choice"))
    while(n<1 or n>2):
        print("Wrong choice TRY AGAIN")
        n=int(input("RE-ENTER YOUR CHOICE"))
    if(n==1):
        p[0]='X'
        p[1]='O'
    else:
        p[0]="O"
        p[1]="X"
p=['-','-']
inputing(p)
l=[1,2,3,4,5,6,7,8,9]
c=0
flag=0
display(l)
print("RESPECTIVE PLAYER NEEDS TO ENTER THE POSITION TO FULLFILL HIS\HER TURN\n")
while(flag<9):
    pos=int(input("Player 1 your turn "))
    while(l[pos-1]=='X'or l[pos-1]=='O'):
        print("Wrong position TRY AGIAN")
        pos=int(input("Player 1 your turn "))
    l[pos-1]=p[0]
    flag+=display(l)
    if(check(l)==1):
        c=1
        break
    if(flag>8):
        break
    pos=int(input("Player 2 your turn "))
    while(l[pos-1]=='X'or l[pos-1]=='O'):
        print("Wrong position TRY AGIAN")
        pos=int(input("Player 2 your turn "))
    l[pos-1]=p[1]
    flag+=display(l)
    if(check(l)==1):
        c=-1
        break
if(c!=1 and c!=-1):
    print("draw")
elif(c==1):
    print(p[0],"is the winner")
else:
    print(p[1],"is the winner")
