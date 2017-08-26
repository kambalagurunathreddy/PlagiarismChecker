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
"""
def lcs(str1,str2):
    len1=len(str1)
    len2=len(str2)
    if len1==0 or len2==0:
        return 0
    else:
        lenLCS,minIndex=0,0
        mini=min(len1,len2)
        maxi=max(len1,len2)
        print(mini,maxi)
        arraysList=genArraysList(mini,maxi)
        if str1>str2:
            str2,str1=str1,str2
        for i in range(mini):
            for j in range(maxi):
                if str1[i]==str2[j]:
                    if i>0 and j>0:
                        arraysList[i][j]=arraysList[i-1][j-1]+1
                        temp=arraysList[i][j]
                        if temp>lenLCS:
                            lenLCS=temp
                            minIndex=i
                    else:
                        arraysList[i][j]=1
                else:
                    arraysList[i][j]=0
    return arraysList,temp,i
"""
def lcs(str1,str2):
    if len(str1)>len(str2):
        str2,str1=str1,str2
    print("str1 : ",str1,"str2 : ",str2)
    len1=len(str1)
    len2=len(str2)
    if len1==0 or len2==0:
        return (None,None,None)
    else:
        lenLCS,minIndex=0,0
        mini=min(len1,len2)
        maxi=max(len1,len2)
        #print(mini,maxi)
        arraysList=genArraysList(mini,maxi)
        for i in range(mini):
            for j in range(maxi):
                #print("\n",arraysList)
                #print(str1[i],str2[j])
                if str1[i]==str2[j]:
                    #print(i,j)
                    if i>0 and j>0:
                        arraysList[i][j]=arraysList[i-1][j-1]+1
                    else:
                        arraysList[i][j]=1
                    temp=arraysList[i][j]
                    if temp>lenLCS:
                        lenLCS=temp
                        minIndex=i
                else:
                    arraysList[i][j]=0
                #else:
                    
                            
                    # else:
                        # arraysList[i][j]=0
        #(str1[-(lenLCS+mini-minIndex):-(mini-minIndex-1)])
        lcString=str1[minIndex+1-lenLCS:minIndex+1]
        strippedLcString=lcString.strip()
        return arraysList,lenLCS,minIndex,lcString,strippedLcString
if __name__=="__main__":        
    str1=" gurunath "
    str2="kambala gurunath reddy"
    matrix,lenL,index,lcstring,strippedlcstring=lcs(str1,str2)
    #lenL=lcs(str1,str2)[1]
    #index=lcs(str1,str2)[2]
    printMatrix(matrix) if matrix!=None else print(None)
    print("Length of longest substring :",lenL)
    print("Longest common substring ends at position: ",index)
    print("Longest common substring : ",lcstring)
    print("Longest common stripped substring : ",strippedlcstring)
    print("Length of Longest common stripped substring : ",len(strippedlcstring))