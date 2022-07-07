import os
import shutil
import fnmatch

original = r"C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\skins"
target = r'C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\mobin'

folder = os.path.join(original,"koopa")
temp_dest = os.path.join(target,"koopa")
shutil.move (folder,temp_dest)


