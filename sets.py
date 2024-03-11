set1 = set(input("Enter integers for the first set separated by spaces: ").split(","))
set2 = set(input("Enter integers for the second set separated by spaces: ").split(","))


common_elements = set1.intersection(set2)

print("Common elements:", common_elements)
