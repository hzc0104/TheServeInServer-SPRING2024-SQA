import os

import subprocess

import shutil

import time

from datetime import datetime

# Method 1: Fuzz giveTimeStamp() Method

def fuzz_giveTimeStamp():

    def giveTimeStamp():

        tsObj = time.time()

        strToret = datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')

        return strToret
 
    print(giveTimeStamp())
 
# Method 2: Fuzz deleteRepo() Method

def fuzz_deleteRepo():

    def deleteRepo(dirName, type_):

        print(':::' + type_ + ':::Deleting ', dirName)

        try:

            if os.path.exists(dirName):

                shutil.rmtree(dirName)

                print("Directory", dirName, "deleted successfully.")

            else:

                print("Directory", dirName, "does not exist.")

        except Exception as e:

            print("Failed deleting directory:", e)
 
    fuzz_dirName = "test_directory"

    fuzz_type = "TEST_TYPE"

    deleteRepo(fuzz_dirName, fuzz_type)
 
# Method 3: Fuzz dumpContentIntoFile() Method

def fuzz_dumpContentIntoFile():

    def dumpContentIntoFile(strP, fileP):

        fileToWrite = open(fileP, 'w')

        fileToWrite.write(strP)

        fileToWrite.close()

        return str(os.stat(fileP).st_size)
 
    fuzz_strP = "Test content to write into file."

    fuzz_fileP = "test_file.txt"

    print("File size after writing:", dumpContentIntoFile(fuzz_strP, fuzz_fileP))
 
# Method 4: Fuzz makeChunks() Method

def fuzz_makeChunks():

    def makeChunks(the_list, size_):

        for i in range(0, len(the_list), size_):

            yield the_list[i:i + size_]
 
    fuzz_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fuzz_size = 3

    for chunk in makeChunks(fuzz_list, fuzz_size):

        print(chunk)
 
# Method 5: Fuzz cloneRepo() Method

def fuzz_cloneRepo():

    def cloneRepo(repo_name, target_dir):

        cmd_ = "git clone " + repo_name + " " + target_dir

        try:

            subprocess.check_output(['bash', '-c', cmd_])

            print("Repository cloned successfully:", repo_name)

        except subprocess.CalledProcessError:

            print('Skipping this repo ... trouble cloning repo:', repo_name)
 
    fuzz_repo_name = "https://github.com/username/repository.git"

    fuzz_target_dir = "/path/to/target_directory"

    cloneRepo(fuzz_repo_name, fuzz_target_dir)
 
if __name__ == "__main__":

    fuzz_giveTimeStamp()

    fuzz_deleteRepo()

    fuzz_dumpContentIntoFile()

    fuzz_makeChunks()

    fuzz_cloneRepo()
