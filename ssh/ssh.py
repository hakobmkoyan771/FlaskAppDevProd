#!/usr/bin/pytihon3
import datetime
import os
import time
import schedule


#Function  that deletes all files except the last three days
def os_path(path):
    day = datetime.datetime.now() - datetime.timedelta(days=2)
    third_day  = day.strftime("%Y-%m-%d %H:%M:%S")
    dirs = os.listdir(path)
    for fil in dirs:
        path_folder = os.path.abspath(fil)
        crate_date = datetime.datetime.fromtimestamp(os.path.getctime(path_folder)).strftime('%Y-%m-%d %H:%M:%S')
        if crate_date >= third_day:
            pass
        else:
            os.remove(path_folder)


def result():
    result = os.system("bash ssh.sh")
    if result == 0:
        path = os.getcwd()
        folder_path = os.path.join(path,"backup")
        os.chdir(folder_path)
        path_folder = os.getcwd()
        os_path(path_folder)
    



def main():
    result = os.system("bash ssh.sh")
    if result == 0:
        path = os.getcwd()
        folder_path = os.path.join(path,"backup")
        os.chdir(folder_path)
        path_folder = os.getcwd()
        os_path(path_folder)

       


if __name__== "__main__":
    main()
   

