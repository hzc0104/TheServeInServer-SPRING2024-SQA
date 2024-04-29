import subprocess
import os
import shutil
import time
from datetime import datetime

#This method is fuzzing for a timestamp that follows along with generic time display.
def fuzz_giveTimeStamp():
    def giveTimeStamp():
        ts = time.time()
        str = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        return str
    print(giveTimeStamp())

#This method is fuzzing the deletion of a repos whether done or not. 
def fuzz_deleteRepo():
    def deleteRepo(dirName, typeA):
        print(':::' + typeA+ ':::Deleting ', dirName)
        try:
            if os.path.exists(dirName):
                shutil.rmtree(dirName)
                print("Directory", dirName, "is deleted now.")
            else:
                print("Directory", dirName, "isn't here y'all.")
        except Exception as e:
            print("Failure in deleting directory:", e)
 
    fuzz_dirName = "test_directory"
    fuzz_typeA = "test_type"
    deleteRepo(fuzz_dirName, fuzz_typeA)
 
#This third method is related to whether the content was actually put into the file or not.

def fuzz_dumpContentIntoFile():
    def dumpContentIntoFile(sP, fP):
        fileToWrite = open(fP, 'w')
        fileToWrite.write(sP)
        fileToWrite.close()
        return str(os.stat(fP).st_size)
    fuzz_sP = "Testing if it worked for content to write into file."
    fuzz_fP = "test_file.txt"
    print("Once writte, your file size is:", dumpContentIntoFile(fuzz_sP, fuzz_fP))
 
# This fourth methid is fuzzing the makeChunks method
def fuzz_makeChunks():
    def makeChunks(aList, sizeA):
        for i in range(0, len(aList), sizeA):
            yield aList[i:i + sizeA]
    fuzz_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fuzz_size = 3
    for chunk in makeChunks(fuzz_list, fuzz_size):
        print(chunk)
 
# This fifth method is just fuzzing on the method for the cloneRepo 
def fuzz_cloneRepo():
    def cloneRepo(repoName, targetDir):
        cmdA = "git clone " + repoName + " " + targetDir
        try:
            subprocess.check_output(['bash', '-c', cmdA])
            print("Repository cloned successfully:", repoName)
        except subprocess.CalledProcessError:
            print('Skipping this repo ... trouble cloning repo:', repoName)
 
    fuzz_repoName = "https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA"
    fuzz_targetDir = "TheServeInServer-SPRING2024-SQA/MLForensics-farzana"

    cloneRepo(fuzz_repoName, fuzz_targetDir)
 
if __name__ == "__main__":
    fuzz_giveTimeStamp()
    fuzz_deleteRepo()
    fuzz_dumpContentIntoFile()
    fuzz_makeChunks()
    fuzz_cloneRepo()
