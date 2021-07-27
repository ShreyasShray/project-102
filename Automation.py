# By this python code you can delete those files which are not accessed for long time.


# importing all the modules
import os
import time
from datetime import datetime

# getting the current timestamp
current_time = time.time()

# taking folder path from user
folder_path = input("Enter the path of the folder which you want to upload and delete, enter the path correctly:\n")
if(os.path.exists(folder_path)):
    # taking number of days from user
    no_of_days = float(input("Enter the number of days for last accessed time of file:\n"))
    if(no_of_days == ""):
        print("number of days not given")
        exit()
else:
    print("File not Found")
    exit()

# getting all files inside the subfolder also
folder_path = os.walk(folder_path)

# for loop to delete files
for root, directories, files in folder_path:
    for fil in files:
        file_path = os.path.join(root, fil)
        # getting accessed time for file
        file_accessed_time = os.stat(file_path).st_atime
        accessed_time_with_given_days = file_accessed_time + (no_of_days*24*60*60)
        # if file accessed time + given time is smaller than the current time then delete files
        if(current_time - accessed_time_with_given_days > 0):
            os.remove(file_path)
            print("Last accessed", datetime.fromtimestamp(file_accessed_time))
            print(fil, " Deleted")
        else:
            print("Last accessed", datetime.fromtimestamp(file_accessed_time))
            print(fil, " accessed recently")