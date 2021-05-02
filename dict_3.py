# Delete a particular product in Dictionary

products={'apple':100,'grapes':200,'orange':60,'banana':50}

#l=products.keys()
for x,y in products.items():
    if x=='banana':
        del products[x]
        break
print(products)
