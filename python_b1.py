import os

# Write a small Python script that takes a hypothetical file path string:
# Your script needs to extract and print out two separate things from this string:
#
# The name of the file itself (main.py).
#
# The name of only the folder that holds it (project_1).

path = "/home/pranaw_rai/Documents/Python/Books/python_2nd.pdf"
print(f"The name of file is: {os.path.basename(path)}")
folderPath = os.path.dirname(path)
folderName = os.path.basename(folderPath)
print("The name of dir is: ", folderName)