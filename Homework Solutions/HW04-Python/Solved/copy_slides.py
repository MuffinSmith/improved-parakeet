# Create a python function that searches for slides in the Downloads folder
# Copy those slides into the current directory

# os module will help us navigate our working directories
# shutil module supports high level file operations like copying
import os
import shutil
# set the download directory for the current user

def pptx_copy():
    download_directory = os.path.expanduser("~/Downloads")
    # set the current directory
    current_directory = os.getcwd()
    # use a for loop to go through all of the files in the downloads directory
    for i in os.listdir(download_directory):
        # set i as the file path
        i = os.path.join(download_directory, i)
        # if the file extension indicates that its a powerpoint
        if i.endswith(".pptx") or i.endswith(".ppt"):
            # use the shutil module to copy the file to the current directory
            shutil.copy2(i, current_directory)

pptx_copy()
