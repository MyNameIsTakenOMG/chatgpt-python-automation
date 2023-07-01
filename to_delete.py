

import os
import shutil
import time

# path to the download folder
download_folder = 'C:/Users/Downloads'

# path to the toDelete folder
to_delete_folder = 'C:/Users/toDelete'

# get the current time in seconds
current_time = time.time()

# loop through the download folder
for file in os.listdir(download_folder):
    # get the path of the file
    file_path = os.path.join(download_folder, file)
    # get the modification time of the file in seconds
    modification_time = os.path.getmtime(file_path)
    # check if the difference between current time and modification time is greater than 30 days
    if current_time - modification_time > (30 * 24 * 60 * 60):
        # move the file to the toDelete folder
        shutil.move(file_path, to_delete_folder)