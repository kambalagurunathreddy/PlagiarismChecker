import os,glob,math,re
from libraries.files.htmlGenerator import *
from libraries.files.fileOperations import *
from libraries.algos.lcs_v1 import *
currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
def getPlagiarismPercent2(file1,file2): 
    """
        Takes two files and calculates plagiarism percentage using Longest common substring algorithm
    """
    print("File1 : ",getFilename(file1))
    print("File2 : ",getFilename(file2))
    file1Contents=getFileContents(file1,ignoreSpecialChars=False) #getting the contents of file 1
    file2Contents=getFileContents(file2,ignoreSpecialChars=False) # getting the contents of file 2
    len1=len(file1Contents)
    len2=len(file2Contents)
    if len1==0 and len2==0:
        print("Plagiarism Percentage : ",0)
        print("As both files are empty")
        return None
    if len1==0 or len2==0:
        print("Plagiarism Percentage : ",0)
        print("As one of the files is empty")
        return None
    temp=lcs(file1Contents,file2Contents)
    if len(temp)>3:
        matrix,lenL,index,lcstring,strippedlcstring=temp
        print("Length of longest substring :",lenL)
        print("Longest common substring ends at position: ",index)
        print("Longest common substring : ",lcstring)
        print("Longest common stripped substring : ",strippedlcstring)
        print("Length of Longest common stripped substring : ",len(strippedlcstring))
        totalLen=(len1+len2)
        print("Total Len",totalLen)
        pPercentage=((len(strippedlcstring)*2)/(totalLen))*100
        print("Plagiarism Percentage : ",pPercentage)
        print("\n")
        return pPercentage
    
    
if __name__=="__main__":
    print ("\n\t\tWelcome\n")
    currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
    print("currentDirABSPath",currentDirABSPath)
    #sourceFolder=input("Enter Folder Absolute Path")
    filesList=getFilesList("txt",currentDirABSPath=currentDirABSPath,sourceFolder="SourceFiles") #getting the files list from given folder
    print("\nFiles list",filesList,"\n")
    totalNoofFiles=len(filesList)
    matrix=genArraysList(totalNoofFiles+1,totalNoofFiles+1,defaultValue="")#creating a template for matrix
    matrix[0][1:]=[(os.path.split(i)[1]).rjust(10) for i in filesList]  #matrix header
    a=1
    for i in filesList:
        b=1
        matrix[a][b-1]=os.path.split(i)[1]
        for j in filesList:
                      
            if j>i:
                temp=getPlagiarismPercent2(i,j) #calculating plagiarism percent
                if temp!=None:
                    matrix[a][b]=round(temp,2)
                else:
                    matrix[a][b]="0 [Empty File(s)]"
                print("------------------------------------------------") 
                print("\n")
            elif j==i:
                matrix[a][b]=100.0
            else:
                matrix[a][b]=matrix[b][a]
            b+=1
            
        a+=1
    printMatrix(matrix)
    htmlGenerator(matrix,currentDirABSPath+os.sep+"Plagiarism Results_LCS.html",title="Plagiarism Checker using LCS Algorithm")   #creating html file with plagiarism results 
    print("\n\n\t\t Please check the Plagiarism Results_LCS.html generated in the current folder")    
            
    
        
