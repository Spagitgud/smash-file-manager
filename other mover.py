import os
import shutil
import fnmatch

original = r"C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\skins"
target = r'C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\mobin'

files = os.listdir(original)
#print(files)

for f in files:
    shutil.move(original+f,target+f)
print("ya paso chele")