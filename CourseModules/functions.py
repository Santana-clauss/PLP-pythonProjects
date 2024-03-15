def address(**kwargs):
    #print(kwargs)
    for k, v in kwargs.items():
        print(f"{k} : {v}")
print(address(name="John", age=30,city="nairobi",country="kenya"))


#lambda functions
#lambda parameters:expression
vote=lambda age:"you can vote" if age>=18 else "note eligible to vote"
print(vote(12))

#builtin functions
student=dict()

student['name']=input("Enter your name: ")
student['age']=input("Enter your age: ")
print(student)