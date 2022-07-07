import os
import shutil
import fnmatch
import glob

original = r"C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\skins"
target = r'C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\mobin'

#pattern='*koopa*'

src_files = os.listdir(original)

#folder = "koopa"

pattern = r"C:\Users\laptoptest\Desktop\Python Memes\Smash File Manager\skins\**\koopa"

#for folders in glob.glob(pattern,recursive=True):
    #print ((folders)+' is true!')
    #print(src_files)


for folders in glob.glob(pattern,recursive=True):
    #print ((folders)+' is true!')
    if True:
        #print (f"{folders} koopa time")
        #os.chdir(original)
        print(folders)
        #shutil.move (original,target)
        
        #file_folder = os.path.join(original,folders)
        #shutil.move(file_folder,target)
        #shutil.move(src_files,target)
        
        

    else:
        print("nel chele")
