import os

path = '/home/nhatminh/Documents/Data/source_media'

def changeDirectory():
    # path = '/home/nhatminh/Documents/Data/source_media'
    os.getcwd()
    os.chdir(path)
    print(os.getcwd())

def listAllFiles():
    entries = os.listdir(path)
    # print(entries)
    return entries

def separateFilenameAndExtension():
    setFilename = set()
    setExtension = set()
    
    lstAllFiles = listAllFiles()
    for file in lstAllFiles:
        # for files, extensionFile in os.path.splitext(file):
        # setFilename.add(os.path.splitext(files)[0])
        # setExtension.add(os.path.splitext(files)[1])
            # print(files)
            # print(extensionFile)    
            # print("----------------")
        print(file)
        # print(os.path.splitext(file)[1])
        if (os.path.splitext(file)[1] != ''):
            setExtension.add(os.path.splitext(file)[1])

    # print(setExtension)
    return setExtension
    # print(setExtension)

def createFolderwithExtension():
    setExtensionForCreateFolder = separateFilenameAndExtension()
    # print(setExtensionForCreateFolder)
    for file in setExtensionForCreateFolder:
        os.mkdir(path + '/' + file[1:])

def moveFile():
    lstFileUseForMove = listAllFiles()
    # print(lstFileUseForMove)
    for file in lstFileUseForMove:
        if (os.path.splitext(file)[1] == ''):
            continue
        else:
            oldPath = path + '/' + file
            newPath = path + '/' + os.path.splitext(file)[1][1:] + '/' + file
            # print(oldPath)
            # print(newPath)
            # print("___________________________")
            os.rename(oldPath, newPath)
def main():
    # changeDirectory()
    # listAllFiles()
    # separateFilenameAndExtension()
    createFolderwithExtension()
    moveFile()

if __name__ == "__main__":
    main()    