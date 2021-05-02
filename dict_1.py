# Getting items for dictionary at run time

register={}

 while True:
    name=input("Enter your name")
    mark=int(input("ENter your mark"))
    register[name]=mark
    NextCandidate=input("Yes/No ")
    if NextCandidate=='No':
        break
    
print(register)
