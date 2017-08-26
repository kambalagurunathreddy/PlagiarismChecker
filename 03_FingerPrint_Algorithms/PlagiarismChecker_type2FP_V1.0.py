import os,glob,math,re
from libraries.files.htmlGenerator import *
from libraries.files.fileOperations import *
from libraries.algos.winnowing_v1 import *
from libraries.misc import *
currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
def getPlagiarismPercent4(file1,file2,n=4,unit=0): #using Type1 FingerPrinting
    """
        given two files, and n-Gram number n , calculates Plagiarism percentage using type-1 FingerPrinting method
        Type-1 usually involves generating hashes for the n-grams generated from file contents and getting the common no.of hashvalues
        Using the count of common hash values, we estimate plagiarism percentage
        
        unit=0, generating nGrams at char level
        unit=1, generating nGrams at word level
    """
    print("File1 : ",getFilename(file1))
    print("File2 : ",getFilename(file2))
    file1Contents=getFileContents(file1,ignoreSpecialChars=False) #getting the contents of file 1
    file2Contents=getFileContents(file2,ignoreSpecialChars=False) #getting the contents of file 2
    pureWords1=getPureWords(file1Contents,stopWordsFilePath=currentDirABSPath+r"\libraries\files\stopwords.txt") #words of file 1 without stop words
    pureWords2=getPureWords(file2Contents,stopWordsFilePath=currentDirABSPath+r"\libraries\files\stopwords.txt") #words of file 2 without stop words
    file1Contents="".join(pureWords1)
    file2Contents="".join(pureWords2)
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
    nGrams1=(nGramGenerator(file1Contents,n=n,unit=unit)) #creating n-Grams
    nGrams2=(nGramGenerator(file2Contents,n=n,unit=unit)) #creating n-Grams
    #print("nGrams1 : ",nGrams1)
    #print("nGrams2 : ",nGrams2)
    hashes1=list(i.genHash(n) for i in nGrams1)
    hashes2=list(i.genHash(n) for i in nGrams2)
    print(hashes1,hashes2)
    commonNgrams=intersect(nGrams1,nGrams2)
    print(commonNgrams)
    pPercent=((len(commonNgrams)*2)/(len(nGrams1)+len(nGrams2)))*100
    print("Plagiarism Percentage : ",pPercent)
    return pPercent
  
if __name__=="__main__":
    print ("\n\t\tWelcome\n")
    currentDirABSPath=os.path.split(os.path.abspath(__file__))[0]
    print("currentDirABSPath",currentDirABSPath)
    #sourceFolder=input("Enter Folder Absolute Path")
    filesList=getFilesList("txt",currentDirABSPath=currentDirABSPath,sourceFolder="SourceFiles")
    print("\nFList",filesList,"\n")
    totalNoofFiles=len(filesList)
    matrix=genArraysList(totalNoofFiles+1,totalNoofFiles+1,defaultValue="")#creating a template for matrix
    matrix[0][1:]=[(os.path.split(i)[1]).rjust(10) for i in filesList]  #matrix header
    a=1
    for i in filesList:
        b=1
        matrix[a][b-1]=os.path.split(i)[1]
        for j in filesList:
                      
            if j>i:
                temp=getPlagiarismPercent4(i,j,n=4,unit=0) #calculating plagiarism percent
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
    htmlGenerator(matrix,currentDirABSPath+os.sep+"Plagiarism Results_Type1FP.html",title="Plagiarism Checker using Type1 Finger Printing Algorithm")   #creating html file with plagiarism results
    print("\n\n\t\t Please check the Plagiarism Results_Type1FP.html generated in the current folder")
    st="a about raju sharma"
    t=getPureWords(st,stopWordsFilePath=currentDirABSPath+r"\libraries\files\stopwords.txt")
    print(t)
    
    
        
