import os
import glob
import shutil
import create_notes_drs

create_notes_drs.main()

for file in glob.glob(os.environ['HOME'] +"/Downloads/**/*.ppt*", recursive=True):
    shutil.copy(file, "CyberSecurity-Notes/")