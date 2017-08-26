import os,glob,math,re
from operations import *
from htmlGenerator import *
global currentDirABSPath  
currentDirABSPath=os.path.split(os.path.abspath(__file__))[0] #to get the exact location from where our python file is run
def getFilesList(*fileExt,sourceFolder=currentDirABSPath,currentDirABSPath=(os.path.split(os.path.abspath(__file__))[0])):
    """
    returns the files list(of the given file extensions) from the given sourceFolder
    if no arguments are passed, the function considers currentDirABSPath as the source folder
    """
    sourceFolderABSPath=os.path.join(currentDirABSPath,sourceFolder);
    stringtoGetTxts_List=[]
    fileExt=(os.path.join(sourceFolder,"*") if len(fileExt)==0 else fileExt) #to take all files, if no fileExt is passed
    for i in fileExt:
        temp=getAbsFilepath(os.path.join(sourceFolder,"*"+i)) #to generate reg expressions to get files of particular extension
        stringtoGetTxts_List.extend(glob.glob(temp))
    filesList=[]
    for i in stringtoGetTxts_List:
        filesList.append(i)
    return filesList
def printDict(d):# useful to print a given dictionary on to console
    print("\n",d)
    for i in d:
        print(i," : ",d[i])
def getAbsFilepath(a):# to get the absolute file path of the given file a
    temp=str(os.path.join(currentDirABSPath,a))
    return temp
def getFilename(filepath):#to 
    return os.path.split(filepath)[1]
def getFreqDict(filePath,caseSensitive=False,ignoreSpecialChars=True): #to create dictionary with words as its keys and frequencies as values 
    """
        creates a dictionary from the file contents using words as its keys and frequencies as values 
    """
    ABSFilePath=filePath
    try:
        file=open(ABSFilePath,"r")
        fileContents=file.read()
        if not caseSensitive: #using case sensitivity mode
            fileContents=fileContents.lower()
        if ignoreSpecialChars:#using special characters mode
            fileContents=re.sub(r"\W"," ",fileContents)
        words=fileContents.split()#creating words list
        freqDict={}
        for i in words:
            if i not in freqDict:
                freqDict[i]=1
            else:
                freqDict[i]+=1
        return freqDict
    except UnicodeDecodeError as e:#ignoring non-text file extensions
        print("\nThe program can't handle proprietary files.Skipping",getFilename(filePath),"\n")
        return -999
    except:
        print("Input Error")
        
def getPlagiarismPercent(file1,file2):
    """
        Takes two files and calculate plagiarism percent using bag of words algorithm
    """
    print("File1 : ",getFilename(file1))
    print("File2 : ",getFilename(file2))
    dict1=getFreqDict(file1) #creating frequency dictionary of file1
    dict2=getFreqDict(file2) #creating frequency dictionary of file2
    if len(dict1)>0 and len(dict2)>0:
        eN1=euclideanNorm(dict1) #calculating euclideanNorm for dict1
        eN2=euclideanNorm(dict2) #calculating euclideanNorm for dict2
        dProduct=dotProduct(dict1,dict2)
        eNormProduct=(eN1*eN2)
        print("Dot Product",dProduct)
        print("Euclidean Norm Product",eNormProduct)
        try:
            theta=math.acos(dProduct/eNormProduct) #calculating theta
        except ValueError:
            dProduct=round(dProduct)
            eNormProduct=round(eN1*eN2)
            theta=math.acos(dProduct/eNormProduct)
        theta=round(theta,2)
        MAX=math.pi
        #print("MAX : ",MAX)
        #return ("Plagiarism Percent : %d"%((abs(theta-MAX)/MAX)*100))
        #return (abs(theta-MAX)/MAX)*100 #calculating Absolute percentage
        return (dProduct/(eNormProduct))*100
        #print(theta)
        #return ("Mentor's Value:"+str(dProduct/(eN1*eN2)))
    else:
        return 0
if __name__=="__main__":
    print ("\n\t\tWelcome\n")
    currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
    print("currentDirABSPath",currentDirABSPath)
    #sourceFolder=input("Enter Folder Absolute Path")
    filesList=getFilesList("txt",sourceFolder="SourceFiles")
    #print("\nFList",filesList,"\n")
    filesFreqDicts={}
    for i in filesList:
        temp=getFreqDict(i)
        if temp==-999:
            print("Skipping...",i) #ignoring non-text files
        else:
            filesFreqDicts[i]=temp
    totalNoofFiles=len(filesFreqDicts)
    matrix=genArraysList(totalNoofFiles+1,totalNoofFiles+1,defaultValue="") #creating a template for matrix
    #printDict(filesFreqDicts)
    #for i in  
    matrix[0][1:]=[getFilename(i).rjust(10) for i in filesFreqDicts]       #matrix header
    a=1
    for i in filesFreqDicts:
        b=1
        matrix[a][b-1]=getFilename(i)
        for j in filesFreqDicts:
                      
            if j>i:
                temp=getPlagiarismPercent(i,j) #calculating plagiarism percent
                print(temp)
                matrix[a][b]=round(temp,2)
                
                print("\n")
            elif j==i:
                matrix[a][b]=100.0
            else:
                matrix[a][b]=matrix[b][a]
            b+=1
        a+=1
    printMatrix(matrix)
    htmlGenerator(matrix,currentDirABSPath+os.sep+"Plagiarism Results_BoW.html",title="Plagiarism Checker using Bag of Words Algorithm") #creating html file with plagiarism results
    print("\n\n\t\t Please check the Plagiarism Results_BoW.html generated in the current folder")
        
        
