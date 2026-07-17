import os
from pathlib import Path

#Write a Python script using the modern with open syntax that opens a file named system_status.log in
# append mode ("a") and writes the line "System Check: All systems nominal.\n". After running the script
# two or three times in your editor to let the lines accumulate, include a final code block that opens the
# file in read mode ("r") to read and print out the entire contents of the log.

path = Path("/home/pranaw_rai/PycharmProjects/PythonProject/TextDir/system_status.log")

with open(path, "a") as f:
    f.write("System Check: All systems nominal.\n")

with open(path, "r") as f:
    data = f.read()
    print(data)