import os,glob,re
global currentDirABSPath
currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
def getWords(string,caseSensitive=False,ignoreSpecialChars=True,delimiter=" "):
    if ignoreSpecialChars:
        string=re.sub(r"\W"," ",string)
    if not caseSensitive:
        string=string.lower()
    return string.split(delimiter)
def getPureWords(string,stopWordsFilePath="stopwords.txt"):
    stopWords=getWords(getFileContents(stopWordsFilePath))
    stringWords=getWords(string)
    temp=[]
    for i in stringWords:
        if i not in stopWords:
            temp.append(i)
    return temp
def getFileContents(absFilePath,caseSensitive=False,ignoreSpecialChars=True):
    try:
        absFilePath=absFilePath.strip('"').strip("'")
        f1=open(absFilePath)
        fileContents=f1.read()
        if ignoreSpecialChars:
            fileContents=re.sub(r"\W"," ",fileContents)
        if not caseSensitive:
            fileContents=fileContents.lower()
        return fileContents
    except Exception as e:
        print(e.args)
    else:
        f1.close()
# def getFilesList(*fileExt,sourceFolder=currentDirABSPath,currentDirABSPath=(os.path.split(os.path.abspath(__file__))[0])):
    # """
    # if no arguments are passed, the function considers currentDirABSPath as the source folder
    # """
    # sourceFolderABSPath=os.path.join(currentDirABSPath,sourceFolder);
    # stringtoGetTxts_List=[]
    # #print(fileExt)
    # fileExt=(os.path.join(sourceFolder,"*") if len(fileExt)==0 else fileExt)
    # #print("hello",fileExt)
    # for i in fileExt:
        # #stringtoGetTxts_List.append(os.path.join(sourceFolder,"*"+i))
        # temp=getAbsFilepath(os.path.join(sourceFolder,"*"+i))
        # #print("temp",glob.glob(temp))
        # stringtoGetTxts_List.extend(glob.glob(temp))
    # #print("stringtoGetTxts_List",stringtoGetTxts_List)
    # filesList=[]
    # for i in stringtoGetTxts_List:
        # #print("glo",glob.glob(currentDirABSPath,i))
        # filesList.append(i)
        # #filesList.extend(glob.glob(i))
    # return filesList
def getFilesList2(*fileExt,sourceFolderABSPath):
    """
    if no arguments are passed, the function considers currentDirABSPath as the source folder
    """
    sourceFolder=os.path.split(sourceFolderABSPath)[1]
    stringtoGetTxts_List=[]
    fileExt=(os.path.join(sourceFolder,"*") if len(fileExt)==0 else fileExt)
    for i in fileExt:
        temp=sourceFolderABSPath+os.sep+"*"+i
        stringtoGetTxts_List.extend(glob.glob(temp))
    print("stringtoGetTxts_List",stringtoGetTxts_List)
    filesList=[]
    for i in stringtoGetTxts_List:
        filesList.append(i)
    return filesList
# def getAbsFilepath(a):
    # temp=str(os.path.join(currentDirABSPath,a))
    # return temp
def getFilename(filepath):
    return os.path.split(filepath)[1]
# if __name__=="__main__":
    # print(getFileContents(input("Enter filename")))
def getFilesList(*fileExt,sourceFolder=currentDirABSPath,currentDirABSPath=(os.path.split(os.path.abspath(__file__))[0])):
    """
    if no arguments are passed, the function considers currentDirABSPath as the source folder
    """
    sourceFolderABSPath=os.path.join(currentDirABSPath,sourceFolder);
    stringtoGetTxts_List=[]
    #print(fileExt)
    fileExt=(os.path.join(sourceFolder,"*") if len(fileExt)==0 else fileExt)
    #print("hello",fileExt)
    for i in fileExt:
        #stringtoGetTxts_List.append(os.path.join(sourceFolder,"*"+i))
        temp=getAbsFilepath(os.path.join(sourceFolder,"*"+i),currentDirABSPath)
        #print("temp",glob.glob(temp))
        stringtoGetTxts_List.extend(glob.glob(temp))
    #print("stringtoGetTxts_List",stringtoGetTxts_List)
    filesList=[]
    for i in stringtoGetTxts_List:
        #print("glo",glob.glob(currentDirABSPath,i))
        filesList.append(i)
        #filesList.extend(glob.glob(i))
    return filesList
def getAbsFilepath(a,currentDirABSPath):
    temp=str(os.path.join(currentDirABSPath,a))
    return temp