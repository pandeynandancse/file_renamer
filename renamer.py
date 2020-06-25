import os
import shutil
import glob



#os.chdir('./images/')
# Am I in the correct directory?
# print(os.getcwd())
# print(dir(os))
# Print all the current file names


from pathlib import Path
files =  sorted(Path('./images').iterdir(), key=lambda f: f.stat().st_mtime)

# sort according to creation time
#files =  sorted(Path('./images').iterdir(), key=lambda f: f.stat().st_ctime)

for index, file in enumerate(files):
    # If .DS_Store file is created, ignore it
    if file == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(file)
    print(file_name)

    #older images are first then newer iamges and so on.........
    
    os.rename(file ,str(index) + ".png")

# print(len(os.listdir()))
