import os
import shutil
import fnmatch

original = r"C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\skins"
target = r'C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\mobin'

pattern='*koopa*'

src_files = os.listdir(original)

for file_name in src_files:

    if fnmatch.fnmatch(file_name,pattern)==True:
           full_file_name = os.path.join(original, file_name)
    
           if os.path.isfile(full_file_name):
                shutil.move(full_file_name, target) 