
myList = input("Enter a list of integers separated by spaces: ")
integer_list = [int(x) for x in myList.split()]
total_sum = sum(integer_list)

print("Sum of the integers:", total_sum)
