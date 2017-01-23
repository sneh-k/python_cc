import os

def rename_files():
    file_names=os.listdir(r"C:\Users\kamat_sn\Downloads\prank")
    print (file_names)

    saved_path=os.getcwd()
    print ("Current working directory : "+saved_path)

    os.chdir(r"C:\Users\kamat_sn\Downloads\prank")

    for file_name in file_names:
        new_name=file_name.translate(None,"0123456789")
        os.rename(file_name,new_name)

rename_files()