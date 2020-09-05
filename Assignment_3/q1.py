str=input("ENTER TEH STRING TO CHECK ITS PROPERTIES ")
l=[]
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(0,26):
    l.append(0) 
for i in range(0,26):
    if al[i] in str.lower():
        l[i]=1
if 0 in l:
    print("NOT A PANAGRAM")
else:
    print("PANAGRAM")
