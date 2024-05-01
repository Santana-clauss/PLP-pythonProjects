# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1.\n")
        file.write("Number: 12345\n")
        file.write("Another line with some text.\n")
        print("File 'my_file.txt' created and written successfully.")
except PermissionError:
    print("Permission denied while trying to create or write to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    print("File creation process completed.\n")


# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied while trying to read 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    print("File reading process completed.\n")


# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending line 1.\n")
        file.write("Another line appended.\n")
        file.write("Appended line with a number: 98765\n")
        print("Three lines appended to 'my_file.txt'.")
except PermissionError:
    print("Permission denied while trying to append to 'my_file.txt'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    print("File appending process completed.")
