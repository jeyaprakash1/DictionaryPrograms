# Nummber of occurences of each letter in given list and remove duplicates in that list

name=eval(input("enter your name"))

d={}

for x in name:
    val=d.get(x,0)+1
    d[x]=val
print(d)
l=[]
for y in d.keys():
    l.append(y)
print(l)

