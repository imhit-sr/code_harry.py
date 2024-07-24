# >>>>Day 87(Shutil Module in Python)
# import shutil
# For copying files and directories>>>>
    # shutil.copy(src, dst): Copies a file from src to dst. The destination can be a file or 
    # directory. If dst is a directory, the file will be copied into that directory
    # with the same name
# shutil.copy("main.py","main_copy.py)") 
    #Shutil.copy2 is similar to copy additionally it preserves the metadata
    # like file creation date,last edited and accessed date
    # for folders
    # shutil.copytree("New_folder","MY_tutorial") 

#  Moving and renaming File>>>>
# shutil.move("New_folder/hello.py","my_fol/my_file.py")
# shutil.move("Magic/Dunder.py","Main/my_file.py")
# Deleting an folder directory
    # shutil.rmtree(r"C:\Users\Admin\Desktop\oops_Tutorial\main3.py")
