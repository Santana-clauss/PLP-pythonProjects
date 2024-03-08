marks=80
if marks>=75:
    print("passed")
elif marks<70 and marks>=65:
    print("student failed")
else:
    print("redo exams")



number=int(input("Enter a number : "))

#for  num in myNumbers:
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



while True:
   username=input("enter your name : ")
   password = input('Enter your password : ')
   if username==""or password=="":
       print("enter all the fields")
   else:
       break

print("logged in successfully")
print('hello',username)

