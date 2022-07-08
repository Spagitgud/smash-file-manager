import os
import shutil
import fnmatch

original = r"C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\skins"
target = r'C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\mobin'


pattern='*koopa*'

src_files = os.listdir(original)

#print(src_files)

'''
for folders in src_files:
    if fnmatch.fnmatch(folders,pattern)==True:
        thefolder = os.path.join(original, folders)
        if os.path.isfile(thefolder):
            shutil.move(thefolder, target) 
'''


for files in src_files:
    folder = os.path.join(original,files)
    temp_dest = os.path.join(target,files)
    shutil.move (folder,temp_dest)


moved_files = os.listdir(target)
print(moved_files)

tessstttt