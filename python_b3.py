import os

d1 = "backup_folder"
d2 = "daily_logs"
# def checking(dirOne, dirTwo):
#     if not os.path.exists(f"/home/pranaw_rai/{dirOne}"):
#         os.makedirs(f"/home/pranaw_rai/{dirOne}")
#
#
#     os.chdir(f"/home/pranaw_rai/{dirOne}")
#     if not os.path.exists(f"/home/pranaw_rai/{dirOne}/{dirTwo}"):
#         os.makedirs(f"/home/pranaw_rai/{dirOne}/{dirTwo}")
#
#     os.chdir(f"/home/pranaw_rai/{dirOne}/{dirTwo}")
#     print("The directory created is: ", os.getcwd())
#
# checking(d1, d2)

def checkingDir(dirOne, dirTwo):
    fullPath = f"/home/pranaw_rai/{dirOne}/{dirTwo}"
    os.makedirs(fullPath, exist_ok=True)
    print("The directory chain is ready at: " + fullPath)

checkingDir(d1, d2)


