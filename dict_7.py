# print a letter occurance of 1,1 above and maximum occurance letter.
name=input("enter your name")
d = {}
for x in name:
     val=d.get(x,0)+1
     d[x]=val
print(d)
# list for letter occur only once
l=[]
# list for a letter occur more than once
l2=[]
for y in d.keys():
    if d[y]==1:
        l.append(y)
    else:
        l2.append(y)
print(l)
print(l2)

        
        
        
