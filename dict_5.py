#  print salaries above 25000 and storing names and salaries in separate list

employees={'jeevan':25000,'suman':30000,'ranjith':40000,'ram':18000}

for names,salaries in employees.items():
    if salaries>25000:
        print(salaries)
names=[]
for x in employees.keys():
    names.append(x)
print(names)

salaries=[]
for y in employees.values():
    salaries.append(y)
print(salaries)
