import os
import shutil
path = '/home/nhatminh/Documents/Data/source_media'

def changeDirectory():
    # path = '/home/nhatminh/Documents/Data/source_media'
    os.getcwd()
    os.chdir(path)
    print(os.getcwd())

def listAllFiles():
    entries = os.listdir(path)
    return entries

def separateFilenameAndExtension():
    # setFilename = set()
    setExtension = set()
    
    entries = listAllFiles()
    for files in entries:
        # setFilename.add(os.path.splitext(files)[0])
        setExtension.add(os.path.splitext(files)[1])
    return setExtension

def createFolderwithExtension():
    setExtension = separateFilenameAndExtension()
    for extension in setExtension:
        if extension != '':
            newpath = os.path.join(path,extension[1:])
            os.mkdir(newpath)
            # print(newpath)
            # print(os.path.exists(newpath))

def moveFilesintoNewfolders():
    entries = listAllFiles()
    for files in entries:
        extension = os.path.splitext(files)[1]
        if extension != '':
            oldpath = os.path.join(path, files)
            newpath = os.path.join(path, extension[1:])
            shutil.move(oldpath, newpath)
        # print(files)
        # print("-------------")
        # print(oldpath)
        # print("-------------")
        # print(newpath)
        # print("************************")

def main():
    # changeDirectory()
    # listAllFiles()
    # separateFilenameAndExtension()
    createFolderwithExtension()
    moveFilesintoNewfolders()

if __name__ == "__main__":
    main()