import os
import shutil
import pandas as pd
# Move a file from the directory d1 to d2




os.chdir('./images/')

# Am I in the correct directory?
# print(os.getcwd())

# print(dir(os))
# Print all the current file names


for index, f in enumerate(os.listdir()):
    # If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue

    # file_name, file_ext = os.path.splitext(f)
    # print(file_name)

    #older images are first then newer iamges and so on.........
    os.rename(f ,str(index))


# print(len(os.listdir()))