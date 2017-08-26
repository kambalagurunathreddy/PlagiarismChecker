import os,glob,math,re
# from libraries.files.fileOperations import *
# from libraries.algos.operations_v1 import *
# from libraries.algos.lcs_v1 import *
class Ngram(object):
    def __init__(self,string):
        self.ngram=string
    def genHash(self,n=4):
        try:
            #assert len(string)>0
            length=len(self.ngram)
            totalSum=0
            for i in self.ngram:
                totalSum+=ord(i)*(pow(n,length)-1)
                length-=1
            return totalSum
        except AssertionError as e:
            print(e.args)
            return -999
            
    def __str__(self):
        return self.ngram
def returnList(NgramsList):
        temp=[]
        for i in NgramsList:
            temp.append(Ngram.__str__(i))
        return temp    
def generateFingerprint(hashesList,P=4):
    """
        given a list of hashValues, generate a list of hashvalues which satisfy (HashValue)mod P==0
        and this list of hashvalues is called signature or fingerprint for the document
        We use this signatures of two documents to calculate local similarity (phi)
        (phi)=no of common elements in both fingerprints/total no.of elements in both fingerprints
        Later, they began using dice for Fingerprinting algorithm
        
        the FingerPrint can be empty, if there are no such hashvalue. 
        Hence we go for winnowing algorithm instead of fingerprinting algorithm
        In winnowing algorithm, we caluculate dice coefficient, (Dice(file1,file2))
        Dice(file1,file2)=(2*(no of common elements in both fingerprints))/(total no.of elements in both fingerprints)
        
        
    """
    temp=[]
    for i in hashesList:
        
        if int(i)%4==0:
            print("i , i%4", i)
            temp.append(int(i))
    return temp
    
    
def nGramGenerator(string,n=1,unit=0,caseSensitive=False,ignoreSpecialChars=True):
    """
        input a string
        
        returns a list of n-Grams by taking unit level.
        If unit=0, grams are generated at character level
        If unit=1, grams are generated at word level
        
        
    """
    try:
        assert n>0,unit in (range(2))
        if ignoreSpecialChars:
            string=re.sub(r"\W","",string)
        if not caseSensitive:
            string=string.lower()
        temp=[]
        length=len(string)
        if unit==0:
            for i in range(0,length-n+1):
                #temp.append(string[i:i+n])
                temp.append(Ngram(string[i:i+n]))
            return temp
        if unit==1:
            wordsList=getWords(string)
            length=len(wordsList)
            for i in range(0,length-n+1):
                #temp.append(wordsList[i:i+n])
                temp.append(Ngram(wordsList[i:i+n]))
            return temp
    except AssertionError as e:
        print(e.args)
        return -999
if __name__=="__main__":
    str1="Kambala Gurunath Reddy"
    str1="A do run run run, a do run run"
    nGrams=nGramGenerator("".join(str1.split()),n=4,unit=0)
    print(nGrams)
    for i in nGrams: 
        print(i,i.genHash(4))
