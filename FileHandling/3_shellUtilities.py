# If code fails, clear all the text files except myFile.txt & myName.txt

import os
from os import path
from datetime import datetime
# For using shell utilities function
import shutil

# For archiving files - 
from shutil import make_archive

# For specific archiving functions like in zip format
from zipfile import ZipFile


def main():
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        dst = src + ".modified"
    

        # # now use the shell to make a copy of the file
        # This will only copy the contents of the src file into a new file.
        # The meta data of original file will not be copied
        shutil.copy(src,dst)

        # # copy over the permissions, modification times, and other info
        # The meta data of original file will be copied by this function
        # NOTE: We first need to copy the file and then use copystat() as it dosent create a new file 
        # but adds info of original file into file copied via copy() function
        shutil.copystat(src, dst)

    t = str(datetime.now())
    t = (((t.replace(" ","_").replace(":","_"))).replace('-','_')).replace('.','_')
    if path.exists("textfile.txt"):
        # # rename the original file
        if path.exists("Renamedfile.txt"):
            os.rename("textfile.txt", "Renamedfile_" + t + ".txt")
    else:
        if path.exists("Renamedfile.txt") == False:
                
            f = open("textfile.txt","w+")  
            f.write("Ayush Adarsh" + "\r\n")
            f.close()
            os.rename("textfile.txt", "Renamedfile.txt")

    
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
    else:
        src = path.realpath("Renamedfile.txt")

    # now put things into a ZIP archive
    root_dir,tail = path.split(src)
    print(root_dir,tail)
    # archive(base_name, format, root_dir)
    # 'base_name' is the name of the file to create, minus any format-specific extension;
    # 'format' is the archive format: one of "zip", "tar", "gztar", "bztar", or "xztar".  Or any other registered format.
    # 'root_dir' is a directory that will be the root directory of the archive

    # make_archive() this will put all the data of project directory into arcive file
    shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("testzip.zip","w") as newzip:
      newzip.write("myfile.txt")
      newzip.write("myname.txt")

if __name__ == "__main__":
    main()