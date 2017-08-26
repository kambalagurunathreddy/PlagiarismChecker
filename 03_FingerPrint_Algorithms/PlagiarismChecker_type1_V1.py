import os,glob,math,re
from libraries.files.fileOperations import *
from libraries.algos.winnowing_v1 import *
from libraries.misc import *
currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
def getPlagiarismPercent3(file1,file2,n=4,unit=0): #using Type1 FingerPrinting
    print("File1 : ",getFilename(file1))
    print("File2 : ",getFilename(file2))
    file1Contents=getFileContents(file1,ignoreSpecialChars=False)
    file2Contents=getFileContents(file2,ignoreSpecialChars=False)
    len1=len(file1Contents)
    len2=len(file2Contents)
    print(file1Contents,file2Contents)
    if len1==0 and len2==0:
        print("Plagiarism Percentage : ",0)
        print("As both files are empty")
        return None
    if len1==0 or len2==0:
        print("Plagiarism Percentage : ",0)
        print("As one of the files is empty")
        return None
    nGrams1=returnList(nGramGenerator(file1Contents,n=n,unit=unit))
    nGrams2=returnList(nGramGenerator(file2Contents,n=n,unit=unit))
    print("nGrams1 : ",nGrams1)
    print("nGrams2 : ",nGrams2)
    commonNgrams=intersect(nGrams1,nGrams2)
    print(commonNgrams)
    pPercent=((len(commonNgrams)*2)/(len(nGrams1)+len(nGrams2)))*100
    print("Plagiarism Percentage : ",pPercent)
  
if __name__=="__main__":
    currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
    print("currentDirABSPath",currentDirABSPath)
    #sourceFolder=input("Enter Folder Absolute Path")
    filesList=getFilesList("txt",currentDirABSPath=currentDirABSPath,sourceFolder="SourceFiles")
    print("\nFList",filesList,"\n")
    for i in range(0,len(filesList)-1):
        for j in range(i+1,len(filesList)):
            getPlagiarismPercent3(filesList[i],filesList[j],n=4,unit=0)
            print("------------------------------------------------")
    
        
