# print a letter which is get highest occurence in string

name=input("enter your name")
d = {}
for x in name:
     val=d.get(x,0)+1
     d[x]=val
print(d)
key=list(d.keys())
val=list(d.values())
n=len(val)-1
for y in range(0,n):
    for x in range(0,n):
        if val[x]>val[x+1]:
            val[x],val[x+1]=val[x+1],val[x]
    n-=1
print(val)
for x,y in d.items():
    if y==val[-1]:
        print(x)
        
    
