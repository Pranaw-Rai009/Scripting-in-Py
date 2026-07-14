import os

# Write a script that does the following three things:
# Find and print the name of the operating system (e.g., 'posix' for Mac/Linux, or 'nt' for Windows) using os.name.
# Find and print the Current Working Directory (where the script is running right now). Hint: We talked about this function earlier!
# Look at the path of that current working directory, and count how many characters long that path string is.



# os.name is a built-in attribute that identifies the name of the operating system-dependent module that Python has imported. I
print(os.name)

dirName = os.path.basename(os.getcwd())
print("The name of current working directory is: ", dirName)

# To get the length of a string in Python, use the built-in len() function.
lent = len(dirName)
print("The length of the current working directory is: ", lent)