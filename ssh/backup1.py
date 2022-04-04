import os
import shutil
from datetime import datetime
import zipfile
import inquirer
import tarfile


#Get time
def get_current_date_and_time():
    current_time = datetime.now()
    replace_current_time = str(current_time).replace(" ","_")
    current_date_and_time = replace_current_time.replace(":","_")
    return current_date_and_time

def get_archive_extension():
    questions = [
      inquirer.List('size',
                message="With what extension to archive? ",
                choices=['.zip' , '.tar'],
            ),
]
    answers = inquirer.prompt(questions)
    for values in answers.values():
        return values
        
          
def create_tar(folder_path, current_date_and_time):
    
    tar_name = os.path.basename(folder_path)
    folder_name = tar_name + current_date_and_time + '.tar.gz'
    tFile = tarfile.open(folder_name, 'w')
    files = os.listdir(".")
    for f in files:
        tFile.add(f)
    tFile.close()
    tar_folder_path = folder_path + os.sep + folder_name
    return tar_folder_path
            

def create_zip(folder_path, current_date_and_time):
        archive_folder_name = folder_path + current_date_and_time + '.zip'
        zf = zipfile.ZipFile(archive_folder_name ,"w" , zipfile.ZIP_DEFLATED , allowZip64=True)
        for root , _ , filenames in os.walk(os.path.basename(folder_path)):
            for name in filenames:
                name = os.path.join(root, name)
                name = os.path.normpath(name)
                zf.write(name, name)
        zf.close()
        zip_path = zf.filename
        return zip_path


#Create a directory  and  go to in the directory
def create_folder():
    folder_name = "backup"
    path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(path , folder_name)
    if os.path.exists(folder_path):
        os.chdir(str(folder_path))
    else:
        os.mkdir(folder_path)
        os.chdir(str(folder_path))
    return folder_path

def main():
    folder_path = input("Please input file path: ")
    if  os.path.exists(folder_path):
        current_date_and_time = get_current_date_and_time()
        archive_extension = get_archive_extension()
        if archive_extension == '.zip':
            zp = create_zip(folder_path, current_date_and_time)
        elif archive_extension == '.tar':
            zp = create_tar(folder_path, current_date_and_time)
        fp = create_folder()
        shutil.move(str(zp) , str(fp))
        print("Backup folder is created and folder is archived")
    else: 
        print("Folder path does not exist.")

       
if __name__== "__main__":
    main()







