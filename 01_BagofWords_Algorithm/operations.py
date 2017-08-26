import math
def dictFreq(filePath,caseSensitive=False):
    file=open(filePath,"r")
    fileContents=file.read()
    words=fileContents.split()
    freqDict={}
    for i in words:
        if not caseSensitive:
            i=i.lower()
        if i not in freqDict:
            freqDict[i]=1
        else:
            freqDict[i]+=1
    return freqDict
def euclideanNorm(freqDict):
    temp=0
    for i in freqDict:
        temp+=freqDict[i]**2
    return (math.sqrt(temp))
def dotProduct(freqDict1,freqDict2):
    temp=[]
    product=0
    for i in freqDict1:
        if i not in temp:
            temp.append(i)
    for i in freqDict2:
        if i not in temp:
            temp.append(i)
    for i in temp:
        product+=freqDict1.get(i,0)*freqDict2.get(i,0)
    return product
def genArraysList(a,b,defaultValue=0): 
    """
    
    returns an matrix of zeroes,size aXb kind of object using lists within a list
    
    """
    try:
        assert a>0,b>0
        temp=[]
        for i in range(a):
            temp.append([defaultValue]*b)
        return temp
    except AssertionError:
        print("invalid Values")
        return -999
#print(genArraysList(5,6))
def printMatrix(l):
    try:
        assert len(l)>0
        for i in l:
            for j in i:
                print(str(j).rjust(10),end="")
            print("\n")
    except AssertionError:
        print("invalid Values")
        return -999
if __name__=="__main__":
    dict1=dictFreq("file1.txt")
    dict2=dictFreq("file2.txt")
    eN1=euclideanNorm(dict1)
    eN2=euclideanNorm(dict2)
    dProduct=dotProduct(dict1,dict2)
    print(euclideanNorm(dict1))
    print(euclideanNorm(dict2))
    print(dProduct)
    theta=math.acos(dProduct/(eN1*eN2))
    theta=round(theta,2)
    print("theta :",theta)
    MAX=math.pi
    print("MAX : ",MAX)
    print("Guru's Value %d"%((abs(theta-MAX)/MAX)*100))
    #print(theta)
    print("Mentor Value:",dProduct/(eN1*eN2))
