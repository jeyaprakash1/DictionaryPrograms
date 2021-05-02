# Interchanging keys and values in Dictionary

employees= {'kathiravan':100, 'roy':200, 'sham':300, 'venkat':400 }
employees2= {}
for name,no in employees.items():
    employees2[no]=name
print(employees2)

# 2nd approch

e={'muthu':101,'ramalingam':102}
print(e)
e={y:x for x,y in e.items()}
print(e)


