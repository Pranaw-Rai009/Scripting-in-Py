import os
from pathlib import Path


# ---------- My Original Manual ----------
path = Path("/home/pranaw_rai/PycharmProjects/PythonProject/Basics/raw_users.txt")
file = os.path.basename(path)

f = open(path, "r")
data = f.read()
print(data)
f.close()

f = open(path, "r")
data = f.read()
lines = data.splitlines()

f2path = "/home/pranaw_rai/PycharmProjects/PythonProject/Basics/clean_users.txt"
f2 = open(f2path, "w")
for line in lines:
    ln = line.strip().lower()
    f2.write(ln + "\n")

f2.close()
f.close()

f2 = open(f2path, "r")
print(f2.read())
f2.close()


