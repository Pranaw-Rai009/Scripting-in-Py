import os
import shutil
from pathlib import Path

path = Path("/home/pranaw_rai/Documents/App_Server.qcow2")
dest_path = Path("/home/pranaw_rai/PycharmProjects/PythonProject/Easy_Py/")
shutil.move(path, dest_path)

