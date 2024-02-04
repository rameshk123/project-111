import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/pc/Pictures"
to_dir = "C:/Users/pc/Music/Documents_Files/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension in ['.jpeg','.pdf','.png','.jpg']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name
        if os.path.exists(path2):
            print("moving" + file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving" + file_name + "....")    
            shutil.move(path1,path3)

   

        
