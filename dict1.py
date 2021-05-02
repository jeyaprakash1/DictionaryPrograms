# Create dictionary

d={}
print(type(d))

# add

d[123]='prakash'
#print(d)
d={124:'sowmya',125:'malliga',126:'murugesan'}
print(len(d))
d.get(126)
print(d)
print(d[125])
# Delete
del d[126]
print(d)

d.clear()
print(d)

