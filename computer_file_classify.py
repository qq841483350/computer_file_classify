import os
import shutil
path='./'
files=os.listdir(path)
for f in files:
    folder_name=path+f.split('.')[-1]
    if not os.path.exists(folder_name):
        #['adasd,'png']
        os.makedirs(folder_name)
        shutil.move(f,folder_name)
    else:
        shutil.move(f,folder_name)
