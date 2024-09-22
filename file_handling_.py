# file_handling_assignment.py

# File Creation: Creating a new file and writing to it
try:
    with open("my_file.txt", 'w') as file:
        file.write("Line 1: Hello World!\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python is awesome!\n")
    print("File created and initial content written successfully.")

    # File Reading and Display: Reading the content from the file
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nReading file content:")
        print(content)

    # File Appending: Appending additional lines
    with open("my_file.txt", 'a') as file:
        file.write("Line 4: Appending text.\n")
        file.write("Line 5: 67890\n")
        file.write("Line 6: More Python fun!\n")
    print("Additional lines appended successfully.")

    # Reading the updated content
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("\nUpdated file content:")
        print(updated_content)

# Error Handling: Catching file-related exceptions
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File handling operation completed.")
